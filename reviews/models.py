from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product



# Create your models here.

RATING_CHOICES = [(i, f"{i} ★") for i in range(1, 11)]

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_review')
    text = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s review on  {self.product.name}"

