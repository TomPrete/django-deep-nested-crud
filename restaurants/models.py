from django.db import models
from django.db.models.fields import related

# Create your models here.
class Restaurant(models.Model):
    DISH_TYPE = [
        ('italian', 'Italian'),
        ('mexican', 'Mexican'),
        ('tex-mex', 'Tex-Mex'),
        ('chinese', 'Chinese'),
        ('thai', 'Thai'),
        ('japanese', 'Japanese'),
        ('american', 'American')
    ]
    name = models.CharField(max_length=150)
    cuisine_type = models.CharField(max_length=150, choices=DISH_TYPE)

    def __str__(self):
        return self.name

class Menu(models.Model):
    TYPE_OF_MENU = [
        ('breakfast', 'Breakfast'),
        ('brunch', 'Brunch'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('happy hour', 'Happy Hour'),
        ('late night', 'Late Night')
    ]
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')
    menu_type = models.CharField(max_length=200, choices=TYPE_OF_MENU)

    def __str__(self):
        return self.menu_type

class Dish(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='dishes')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name
