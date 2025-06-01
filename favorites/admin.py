from django.contrib import admin
from favorites.models import *

# Register your models here.



class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
    search_fields = ('user__username', 'product__name')
    list_filter = ('user',)
    ordering = ('user',)

admin.site.register(Favorite, FavoriteAdmin)


