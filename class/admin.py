from django.contrib import admin
from .models import *
from django.contrib.auth.models import Permission

# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    list_display = ['id','username','email']
    search_fields = ['name','phone']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','price','date','status']
    search_fields =['id','name','price']

class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['id','user_id','product_id','quantity','total_price','address']
    search_fields = ['id']

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id','date','method','total_price','transaction_of_customer','transaction_of_merchant']

admin.site.register(User, UsersAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderDetail)
admin.site.register(ShoppingCart, ShoppingCartAdmin )
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Permission)

