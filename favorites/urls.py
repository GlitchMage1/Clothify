from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from favorites.views import *




urlpatterns = [
    path('add/<int:product_id>', add_to_favorite_view, name='add_favorite'),
    path('remove/<int:product_id>', remove_from_favorite_view, name='remove_favorite'),
    path('page', favorite_view, name='favorite')
]