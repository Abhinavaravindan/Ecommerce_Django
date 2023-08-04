from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from.models import Category,Products



def index(request):
   return render(request, 'index.html')

def products(request):
    category=Category.objects.filter(status=0)
    return render(request, 'product.html',{'category':category})
# @login_required(login_url='login')

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
            return redirect('login')
        
        
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
            return redirect('/')
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


def contact(request):
    return render(request,'contact.html')



def blog_list(request):
    return render(request,'blog_list.html')







