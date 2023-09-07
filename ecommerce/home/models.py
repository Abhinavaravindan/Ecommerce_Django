from django.db import models
from django.contrib.auth.models import  User

class Category(models.Model):
    slug=models.CharField(max_length=200,null=False,blank=False)
    name=models.CharField(max_length=40,null=False,blank=False)
    image=models.ImageField(upload_to='imagess')
    status=models.BooleanField(default=False,help_text="0=defualt,1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=defualt,1=Hidden")
    
    def __str__(self):
        return self.name
 
class Products(models.Model):
    category=models.ForeignKey(Category, default='Uncategorized',on_delete=models.CASCADE)
    slug=models.CharField(max_length=200,null=False,blank=False)
    name=models.CharField(max_length=40,null=False,blank=False)
    product_image=models.ImageField(upload_to='product_images',null=False,blank=False, default='default_product_image.jpg')
    description=models.TextField(max_length=500,null=False,blank=False,default='Some default description')
    quantity=models.IntegerField(null=False,blank=False)
    orginal_price=models.DecimalField(decimal_places=2,max_digits=10,null=False,blank=False, default=0.00)
    selling_price=models.FloatField(null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=defualt,1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=defualt,1=Hidden")
    
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE) 
    product =models.ForeignKey(Products,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    

class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE) 
    product =models.ForeignKey(Products,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE) 
    fname=models.CharField(max_length=40,null=False)
    lname=models.CharField(max_length=40,null=False)
    email=models.EmailField(max_length=40,null=False)
    phone=models.CharField(max_length=40,null=False)
    address=models.TextField(null=False)
    city=models.CharField(max_length=40,null=False)
    state=models.CharField(max_length=40,null=False)
    pincode=models.CharField(max_length=40,null=False)
    total_price=models.FloatField(null=False)
    payment_mode=models.CharField(max_length=140,null=False)
    payment_id=models.CharField(max_length=140,null=True)
    orderstatuses= (
        ('Pending','Pending'),
        ('Out For Shipping','Out For Shipping'),
        ('Completed','Completed'),
    )
    status=models.CharField(max_length=140,choices=orderstatuses,default='Pending')
    messege=models.TextField(null=True)
    tracking_no=models.CharField(max_length=150,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{} - {}'.format(self.id,self.tracking_no)
    

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    price=models.FloatField(null=False)
    quantity=models.IntegerField(null=False)
    
    def __str__(self):
        return '{} - {}'.format(self.order.id,self.order.tracking_no)