from django.shortcuts import render, redirect
from .models import Restaurant, Menu, Dish
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

# --- Function Based Views ---
def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    data = {
        'all_restaurants': restaurants,
        'title': 'Restaurant List'
    }
    return render(request, 'restaurants/rest_list.html', data)

def restaurant_detail(request, rest_id):
    restaurant = Restaurant.objects.get(id=rest_id)
    data = {
        'restaurant': restaurant
    }
    return render(request, 'restaurants/rest_detail.html', data)

def menu_list(request, rest_id):
    menus = Menu.objects.filter(restaurant=rest_id)
    data = {
        'menus': menus
    }
    return render(request, 'menus/menu_list.html', data)

def menu_detail(request, rest_id, menu_id):
    menu = Menu.objects.get(id=menu_id)
    rest = Restaurant.objects.get(id=rest_id)
    data = {
        'menu': menu,
        'restaurant': rest
    }
    return render(request, 'menus/menu_detail.html', data)

def dish_list(request, rest_id, menu_id):
    menu = Menu.objects.get(id=menu_id)
    restaurant = Restaurant.objects.get(id=rest_id)
    data = {
        'menu': menu,
        'dishes': menu.dishes.all(),
        'restaurant': restaurant
    }
    return render(request, 'dishes/dish_list.html', data)

def dish_detail(request, rest_id, menu_id, dish_id):
    dish = Dish.objects.get(id=dish_id)
    data = {
        'dish': dish
    }
    return render(request, 'dishes/dish_detail.html', data)



# --- Class Based Views
# class RestaurantListView(ListView):
#     model = Restaurant
#     template_name = "restaurants/rest_list.html"
#     context_object_name = "all_restaurants"

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context["title"] = "Restaurant List"
#         return context


# class RestaurantDetailView(DetailView):
#     model = Restaurant
#     template_name = "restaurants/rest_detail.html"
#     context_object_name = "i"
#     pk_url_kwarg = "rest_id"

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context["title"] = "Restaurant Detail"
#         return context



# class MenuListView(ListView):
#     model = Menu
#     template_name = "restaurants/menu_list.html"
#     context_object_name = "info"

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context["title"] = "Menu List"
#         context["rest_id"] = self.kwargs["rest_id"]
#         return context

#     def get_queryset(self):
#         rest_id = self.kwargs["rest_id"]
#         return Menu.objects.filter(restaurant__id=rest_id)

# class MenuDetailView(DetailView):
#     model = Menu
#     template_name = "restaurants/menu_detail.html"
#     pk_url_kwarg = "menu_id"

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context["title"] = "Menu Detail"
#         return context

#     def get_object(self):
#         menu_id = self.kwargs["menu_id"]
#         return Menu.objects.get(pk=menu_id)

# class DishListView(ListView):
#     model = Dish
#     template_name = "restaurants/dish_list.html"

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context["title"] = "Dish List"
#         context["rest_id"] = self.kwargs["rest_id"]
#         context["menu_id"] = self.kwargs["menu_id"]
#         return context

#     def get_queryset(self):
#         menu_id = self.kwargs["menu_id"]
#         return Dish.objects.filter(menu__id=menu_id)

# class DishDetailView(DetailView):
#     model = Dish
#     template_name = "restaurants/dish_detail.html"
#     pk_url_kwarg = "dish_id"

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context["title"] = "Dish List"
#         return context

#     def get_object(self):
#         dish_id = self.kwargs["dish_id"]
#         return Dish.objects.get(pk=dish_id)
