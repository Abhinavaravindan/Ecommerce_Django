from django.contrib import admin
from.models import Category,Products,Cart,Wishlist,Order,OrderItem

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(OrderItem)