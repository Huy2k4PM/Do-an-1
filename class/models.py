from django.db import models
from django.contrib.auth.models import AbstractUser
import random

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100,unique=True,default='')
    avatar = models.ImageField(upload_to='',blank=True)

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=True)
    image = models.ImageField(null=True,blank=True)
    description = models.TextField()
    status = models.BooleanField(default=False)
    date = models.DateTimeField(blank=False,null=True)

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/static/images/default_product_image.jpg'

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=0, blank =True, default=True)
    address = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

class Payment(models.Model):
    METHOD_CHOICES = [
        ('offline', 'Trực Tiếp'),
        ('online', 'Online'),
    ]
    date = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=10, choices=METHOD_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=0, blank= True)
    transaction_of_customer = models.IntegerField(blank=True) 
    transaction_of_merchant = models.IntegerField(blank=True)

    def save(self, *args, **kwargs):
        self.total_price = self.shopping_cart.total_price
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.transaction_of_customer = random.randint(1,100)
        self.transaction_of_merchant = random.randint(1,100)
        super().save(*args, **kwargs)

    def __str__(self):
        return (self.user.username)
    
class OrderDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0,null=True)
    total_price = models.FloatField(blank=True)
    
    def save(self, *args, **kwargs):
        self.total_price = self.quantity * (self.product.price)
        super().save(*args, **kwargs)
    def __str__(self):
        return (self.user.username)
    
class FeedBack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=50)

    def __str__(self):
        return (self.user.username)