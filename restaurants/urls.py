from django.urls import path
from . import views



urlpatterns = [
    # /restaurants/ list all restaurants
    # /restaurants/:rest_id view restaurant detail
    # /restaurants/:rest_id/menus view restaurants menus
    # /restaurants/:rest_id/menus/:menu_id view menus detail
    # /restaurants/:rest_id/menus/:menu_id/dishes view dish list
    # /restaurants/:rest_id/menus/:menu_id/dishes/:dish_id view dish detail

    # --- Function Based ---
    path('', views.restaurant_list, name='restaurant_list'),
    path('<int:rest_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('<int:rest_id>/menus/', views.menu_list, name='menu_list'),
    path('<int:rest_id>/menus/<int:menu_id>/', views.menu_detail, name='menu_detail'),
    path('<int:rest_id>/menus/<int:menu_id>/dishes/', views.dish_list, name='dish_list'),
    path('<int:rest_id>/menus/<int:menu_id>/dishes/<int:dish_id>/', views.dish_detail, name='dish_detail'),

    # Class Based Views
    # path('', views.RestaurantListView.as_view(), name='restaurant_list'),
    # path('<int:rest_id>/', views.RestaurantDetailView.as_view(), name="rest_detail"),

    # path('<int:rest_id>/menus/', MenuListView.as_view(), name="menu_list"),
    # path('<int:rest_id>/menus/<int:menu_id>/', MenuDetailView.as_view(), name="menu_detail"),

    # path('<int:rest_id>/menus/<int:menu_id>/dishes/', DishListView.as_view(), name="dish_list" ),
    # path('<int:rest_id>/menus/<int:menu_id>/dishes/<int:dish_id>/', DishDetailView.as_view(), name="dish_detail" ),
    # path('<int:rest_id>/menus/<int:menu_id>/dishes/new/', DishCreateView.as_view(), name="dish_create" ),
]
