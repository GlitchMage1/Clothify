from django.core.checks import messages
from django.shortcuts import render, get_object_or_404, redirect

from catalog.models import *
from favorites.models import *
from reviews.models import *
from reviews.views import *
# Create your views here.


def get_latest_product():
    latest_product = Product.objects.order_by('-created_at')[:4]
    return latest_product

def get_products():
    products = Product.objects.all()
    return products


def get_categories():
    categories = Category.objects.all()
    return categories


def catalog_view(request, category_slug=None):
    categories = get_categories()
    products = get_products()

    selected_category = None
    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=selected_category)

    if request.user.is_authenticated:
        favorite_products = Favorite.objects.filter(user=request.user).values_list('product_id', flat=True)
    else:
        favorite_products = []
    context = {
        'categories':categories,
        'products':products,
        'selected_category':selected_category,
        'favorite_products':favorite_products,
    }

    return render(request, 'catalog/catalog.html', context)




def search_view(request):

    querry = request.GET.get('q','').strip().lower()

    products = Product.objects.filter(name__icontains=querry)

    context = {'products':products, 'querry':querry}

    return render(request, 'catalog/search.html', context)



def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    reviews = Review.objects.filter(product=product)

    if request.method == 'POST':
        existing_review = Review.objects.filter(user=user, product=product).first()

        if existing_review:
            existing_review.text = request.POST.get('comment')
            existing_review.rating = request.POST.get('rating')
            existing_review.save()
        else:
            Review.objects.create(
                user=user,
                product=product,
                text=request.POST.get('comment'),
                rating=request.POST.get('rating'),
            )
            # messages.success(request, "Спасибо за ваш отзыв!")


        return redirect('product_detail', product_id=product.id)

    reviews = Review.objects.filter(product=product)



    context = {
        'product':product,
        'reviews':reviews,
        'user':user,

    }



    return render(request, 'catalog/product.html', context)

