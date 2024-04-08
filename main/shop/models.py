from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    url_image = models.URLField(max_length=200)
    subcription = models.TextField()


    def __str__(self):
        return f"ID: {self.pk} | {self.title} | {self.price}₽"


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"ID: {self.pk} | {self.user}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return f"ID: {self.pk} | User: {self.cart.user} | Title: {self.product.title} | Price: {self.product.price}₽ | Quantity: {self.quantity}"
