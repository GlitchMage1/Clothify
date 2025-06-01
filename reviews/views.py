from django.shortcuts import render

from reviews.models import *
# Create your views here.


def get_latest_reviews():
    latest_reviews = Review.objects.order_by('-updated_at')[:6]

    return latest_reviews