from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product

# Create your models here.


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Cart"



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)



    def __str__(self):
        return f"{self.cart.user.username}'s {self.product.name} in Cart"

    @property
    def product_total_cost(self):
        return self.product.price * self.quantity

