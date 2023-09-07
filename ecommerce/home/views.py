from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from.models import Category,Products,Cart,Wishlist,Order,OrderItem
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import random

def index(request):
   return render(request, 'index.html')


def products(request):
    category=Category.objects.filter(status=0)
    return render(request, 'product.html',{'category':category})


def loginn(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid login")
            return redirect('register')
    return render(request,'login.html')


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,"user already exist")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"user already exist")
            return redirect('register')
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save();
            return redirect('login')
    else:
        return render(request,'register.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')


def productview(request,slug):   
    if(Category.objects.filter(slug=slug,status=0)):
        product=Products.objects.filter(category__slug=slug)
    else:
        messages.error(request,"No such a Category")
        return redirect('products')
    return render(request,'collection.html',{'product':product})


def collectionview(request,category__slug,prod_slug):
    if(Category.objects.filter(slug=category__slug,status=0)):
        if(Products.objects.filter(slug=prod_slug,status=0)):
            abhi=Products.objects.filter(slug=prod_slug,status=0)
        else:
            messages.error(request,'no such product found')
            return redirect('products')      
    else:
        messages.error(request,'no  such category found')
        return redirect('products')
    return render(request,'productview.html',{'abhi':abhi})  


def send_email(subject, message, from_email, recipient_list):
    try:
        send_mail(subject, message, from_email, recipient_list)
        return True
    except Exception as e:
        return str(e)
    

def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = f"New message from {email}"
        from_email = 'abhinave953@gmail.com'
        recipient_list = ['abhinave953@gmail.com']
        email_result = send_email(subject, message, from_email, recipient_list)
        if email_result:
             return HttpResponse('Email sent successfully.')
        else:
            return HttpResponse('An error occurred while sending the email.')
    return render(request, 'contact.html')


def blog_list(request):
    return render(request,'blog_list.html')


def about(request):
    return render(request,'about.html')


def addtocart(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            try:
                prod_id = int(request.POST.get('product_id'))
                prod_qty = int(request.POST.get('product_qty'))
                product = get_object_or_404(Products, id=prod_id) 
                if Cart.objects.filter(user=request.user, product_id=prod_id).exists():
                    return JsonResponse({'status': "Product already in cart"})
                if product.quantity >= prod_qty:
                    Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                    return JsonResponse({'status': "Product added successfully"})
                else:
                    return JsonResponse({'status': f"Only {product.quantity} quantity available"})
            except Products.DoesNotExist:
                return JsonResponse({'status': "No such product found"})  
        else:
            return JsonResponse({'status': "Login to continue"})
    return redirect('/')



def viewcart(request):
    cart=Cart.objects.filter(user=request.user)
    context={'cart':cart}
    return render(request,"cart.html",context)
    
    
def deletecartitem(request):   
    if request.method=='POST':
        prod_id = int(request.POST.get('product_id'))
        if (Cart.objects.filter(user=request.user, product_id=prod_id)):
            cartitem= Cart.objects.get(product_id=prod_id,user=request.user)
            cartitem.delete()
        return JsonResponse({'status': "Deleted Successfully"})
    return redirect('/')


def wishlist(request):
    wishlist=Wishlist.objects.filter(user=request.user)
    context={'wishlist':wishlist}
    return render(request,'wishlist.html',context) 

def addtowishlist(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check=Products.objects.get(id=prod_id)
            if(product_check):
                if(Wishlist.objects.filter(user=request.user,product_id=prod_id)):
                    return JsonResponse({'status': "product already in wishlist"})
                else:
                    Wishlist.objects.create(user=request.user,product_id=prod_id )
                    return JsonResponse({'status': "product added to wishlist"})
            else:
                return JsonResponse({'status': "No such product found"})
        else:
            return JsonResponse({'status': "Login to continue"})
    return redirect('/')


def checkout(request):
    rawcart=Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty>item.product.quantity:
            Cart.objects.delete(id=item.id)
            
            
    cartitems=Cart.objects.filter(user=request.user)   
    total_price=0
    for item in cartitems:  
        total_price=total_price+ item.product.selling_price * item.product_qty
        
    context={'cartitems':cartitems,'total_price':total_price}
    
    
    return render(request,'checkout.html',context)


def placeorder(request):
     if request.method=='POST':
         neworder= Order()
         neworder.user=request.user
         neworder.fname=request.POST.get('fname')
         neworder.lname=request.POST.get('lname')
         neworder.email=request.POST.get('email')
         neworder.phone=request.POST.get('phone')
         neworder.address=request.POST.get('address')
         neworder.city=request.POST.get('city')
         neworder.state=request.POST.get('state')
         neworder.pincode=request.POST.get('pincode')
         
         neworder.payment_mode=request.POST.get('payment_mode')
         
         cart=Cart.objects.filter(user=request.user)
         cart_total_price=0
         for item in cart:
             cart_total_price =cart_total_price + item.product.selling_price * item.product_qty
    
         neworder.total_price=cart_total_price
         trackno = 'sharma'+str(random.randint(1111111,9999999))
         while Order.objects.filter(tracking_no=trackno):
             trackno = 'abhi'+str(random.randint(1111111,9999999))
             
         neworder.tracking_no =trackno
         neworder.save()  
         
         neworderitems =Cart.objects.filter(user=request.user)
         for item in neworderitems:
             OrderItem.objects.create(
                 order=neworder,
                 product=item.product,
                 price=item.product.selling_price,
                 quantity=item.product_qty
             )
             #To decrease the product quanity from available stock
             orderproduct=Products.objects.filter(id=item.product_id).first()
             orderproduct.quantity = orderproduct.quantity- item.product_qty
             orderproduct.save()
        
         #to clear the  user cart
         Cart.objects.filter(user=request.user).delete()
         messages.success(request,"yor order has been placed succsfully")
                 
         
     return redirect('/')
 
 
def myorders(request):
    orders=Order.objects.filter(user=request.user)
    context={'orders':orders}
    return render(request,'orders.html',context)


def orderview(request,t_no):
    order=Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitems= OrderItem.objects.filter(order=order)
    context= {'order':order,'orderitems':orderitems}
    return render(request,'orderview.html',context)
                        
                        

def productlistAjax(request):
    products=Products.objects.filter(status=0).values_list('name',flat=True)
    productList=list(products)
    
    return JsonResponse(productList,safe=False)


def searchproduct(request):
    if request.method=='POST':
        searcheditem= request.POST.get('productsearch')
        if searcheditem=="":
            return redirect (request.META.get('HTTP_REFERER'))  
        else:
            product= Products.objects.filter(name_contains=searcheditem).first() 
            
            if product:
                return redirect('products/'+product.category.slug+'/'+product.slug)
            else:
                messages.info(request,"NO products matched your search")
                return redirect (request.META.get('HTTP_REFERER'))
                
            
    return redirect (request.META.get('HTTP_REFERER'))    