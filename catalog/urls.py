from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from catalog.views import *




urlpatterns = [
    path('', catalog_view, name='catalog'),
    path('category/<slug:category_slug>', catalog_view, name='category_products'),
    path('search/', search_view, name='search'),
    path('product/<int:product_id>', product_detail_view, name='product_detail')
]