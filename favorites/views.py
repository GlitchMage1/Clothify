from django.shortcuts import render, get_object_or_404, redirect

from favorites.models import *
from catalog.views import *
# Create your views here.


def add_to_favorite_view(request, product_id):
    user = request.user
    if user.is_authenticated:

        product = get_object_or_404(Product, id=product_id)
        favorite, created = Favorite.objects.get_or_create(product=product, user=user)
        if not created:
            pass


        next_url = request.GET.get('next')
        if next_url:
            return redirect(next_url)
        else:
            return redirect('index')


    else:
        return redirect('login')



def remove_from_favorite_view(request, product_id):
    user = request.user
    if user.is_authenticated:

        Favorite.objects.filter(user=request.user, product_id=product_id).delete()

        next_url = request.GET.get('next')
        if next_url:
            return redirect(next_url)
        else:
            return redirect('index')


    else:
        return redirect('login')



def favorite_view(request):

    user = request.user
    if user.is_authenticated:
        favorites = Favorite.objects.filter(user=request.user).select_related('product')
        products = [fav.product for fav in favorites]

        context = {
            'favorite_products': products
        }
        return render(request, 'favorite/favorite.html', context)









