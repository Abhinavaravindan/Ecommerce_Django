from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('products',views.products,name='products'),
    path('login',views.loginn,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('products/<str:slug>',views.productview,name='productview'),
    path('products/<str:category__slug>/<str:prod_slug>',views.collectionview,name='collectionview'),
    path('contact',views.contact,name='contact'),
    path('blog_list',views.blog_list,name='blog_list'),
    
  

]