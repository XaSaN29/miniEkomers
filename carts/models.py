from django.db import models
from users.models import User
from products.models import Product

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='carts_product')
    quantity = models.IntegerField()
    new_price = models.IntegerField()

    def __str__(self):
        return f'{self.user} - {self.products}'

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.products:
            self.new_price = self.products.price
        super().save(*args, force_insert=force_insert, force_update=force_update, using=using,
                     update_fields=update_fields)

    @property
    def total_price(self):
        self.price * self.new_price

