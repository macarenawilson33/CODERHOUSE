from django.contrib import admin
from .models import Libro, Vinilo, Comics

# Register your models here.
admin.site.register(Libro)
admin.site.register(Vinilo)
admin.site.register(Comics)
