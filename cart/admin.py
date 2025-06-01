from django.contrib import admin
from cart.models import *


# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user__username',)
    list_filter = ('user',)
    ordering = ('user',)

admin.site.register(Cart, CartAdmin)



class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
    search_fields = ('cart__user',)
    list_filter = ('cart', 'product', 'quantity')
    ordering = ('id',)

admin.site.register(CartItem, CartItemAdmin)


