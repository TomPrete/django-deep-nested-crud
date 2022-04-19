from django.contrib import admin
from .models import Restaurant, Menu, Dish
# Register your models here.

admin.site.register([Restaurant, Menu, Dish])
