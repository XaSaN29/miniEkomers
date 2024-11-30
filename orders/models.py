from django.db import models

from products.models import Product, BaseCreatedModel
from users.models import User


# Create your models here.

class Order(BaseCreatedModel):
    class Status(models.TextChoices):

        Shipping = 'Shipping'
        Sent = 'Sent'
        Delivery = 'Delivery'

    class Payment_Method(models.TextChoices):
        OnlinePraise = 'OnlinePraise'
        CashMoney = 'CashMoney'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders_product')
    product_quantity = models.IntegerField()
    total_price = models.IntegerField()
    status = models.CharField(max_length=25, choices=Status)
    payment_method = models.CharField(max_length=25, choices=Payment_Method)

    def __str__(self):
        return f'{self.product.name}'


class OrderItem(BaseCreatedModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_order_item')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def total_price(self):
        return self.quantity * self.price

    def __str__(self):
        return f'{self.product.name}'
