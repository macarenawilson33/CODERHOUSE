from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Product Categories'
'''
class Customer(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='upload/customer/', default='default/avatar.jpg')
    name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name} {self.last_name}'
'''    
class Product(models.Model):
    name = models.CharField(max_length=50) 
    description = models.CharField(max_length=500) 
    price = models.DecimalField(default=0, decimal_places=2, max_digits=12)
    image = models.ImageField(upload_to='upload/product/', default='default/default_product.jpg') 
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, default=1)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return f'{self.name}'
'''
class OrderStatus(models.Model):
    code = models.CharField(max_length=10, default='CREATED') 
    description = models.CharField(max_length=50) 
    models.UniqueConstraint(fields='code',name='order_status_uk')
    def __str__(self):
        return f'[{self.code}]:{self.description}'
    class Meta:
        verbose_name_plural = 'Order Statuses'   

class Order(models.Model):
    quantity = models.DecimalField(default=1, decimal_places=2, max_digits=6)
    date = models.DateTimeField(default=datetime.datetime)
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
'''

class Comment(models.Model):
    comment_content = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
