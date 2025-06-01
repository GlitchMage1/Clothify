from django.shortcuts import render

from reviews.views import *
from catalog.views import *

def index_view(request):
    latest_product = get_latest_product()
    latest_reviews = get_latest_reviews()

    context = {'latest_product': latest_product,
               'latest_reviews': latest_reviews}




    return render(request, 'core/index.html', context)


def about_us_view(request):


    return render(request, 'core/aboutus.html')