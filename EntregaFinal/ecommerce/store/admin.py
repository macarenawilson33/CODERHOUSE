from django.contrib import admin
from .models import ProductCategory,Product,Comment#,Customer,OrderStatus,Order

# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Comment)
#admin.site.register(Customer)
#admin.site.register(OrderStatus)
#admin.site.register(Order)