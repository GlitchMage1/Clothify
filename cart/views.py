from django.core.checks import register
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django import template


from cart.models import *
from favorites.models import *
from catalog.models import *
from core.urls import *

# Create your views here.





def cart_view(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    cart, created = Cart.objects.get_or_create(user=user)
    cart_items = CartItem.objects.filter(cart=cart)


    total_price = sum(item.product.price * item.quantity for item in cart_items)

    context = {
        'cart':cart,
        'cart_items':cart_items,
        'total_price':total_price,


    }


    return render(request, 'cart/cart.html', context)





def add_to_cart_view(request, product_id):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    referer = request.META.get('HTTP-REFERER')

    cart, created = Cart.objects.get_or_create(user=user)
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1

    cart_item.save()


    next_url = request.GET.get('next')
    if next_url:
        return redirect(next_url)
    else:
        return redirect('index')






def cart_item_increase(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.quantity += 1
    item.save()
    return redirect('cart')

def cart_item_decrease(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('cart')

def cart_item_remove(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    return redirect('cart')


register = template.Library()

