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
    path('contact/',views.contact,name='contact'),
    path('blog_list',views.blog_list,name='blog_list'),
    path('about',views.about,name='about'),
    path('send_email/', views.send_email, name='send_email'),
    path('add-to-cat',views.addtocart,name="addtocart"),  
    path('cart',views.viewcart,name="cart"),
    path('delete-cart-item',views.deletecartitem,name="deletecartitem"),
    path('wishlist',views.wishlist,name="wishlist"),
    path('add-to-wishlist-',views.addtowishlist,name="addtowishlist"),
    path('checkout',views.checkout,name="checkout"),
    path('place-oreder',views.placeorder,name="placeorder"),
    path('my-orders',views.myorders,name="myorders"),
    path('view-order/<str:t_no>',views.orderview,name="orderview"),
    path('product-list',views.productlistAjax),
    path('searchproduct',views.searchproduct,name="searchproduct"),
]