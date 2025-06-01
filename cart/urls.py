from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from cart.views import *




urlpatterns = [
    path('', cart_view, name='cart'),
    path('add/<int:product_id>', add_to_cart_view, name='add_to_cart'),
    path('cart/item/<int:item_id>/increase/', cart_item_increase, name='cart_item_increase'),
    path('cart/item/<int:item_id>/decrease/', cart_item_decrease, name='cart_item_decrease'),
    path('cart/item/<int:item_id>/remove/', cart_item_remove, name='cart_item_remove'),

]