from django.db import models

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
    quntity=models.IntegerField(null=False,blank=False)
    orginal_price=models.DecimalField(decimal_places=2,max_digits=10,null=False,blank=False, default=0.00)
    selling_price=models.FloatField(null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=defualt,1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=defualt,1=Hidden")
    
    
    
    def __str__(self):
        return self.name
    
class Contacts(models.Model):
    full_name=models.CharField(max_length=40,null=False,blank=False)
    email=models.EmailField(max_length=254,unique=True,blank=False,null=False,verbose_name='Email Address')
    subject=models.CharField(max_length=40,null=False,blank=False)
    messege= models.TextField( blank=True,null=True,)      
        
        
        
    
    
    
           

