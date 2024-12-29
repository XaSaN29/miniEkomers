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
    product_quantity = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=25, default='Shipping',  blank=True, null=True, choices=Status)
    payment_method = models.CharField(max_length=25, default='OnlinePraise', blank=True, null=True, choices=Payment_Method)

    @property
    def total_price(self):
        return sum(item.total_price for item in self.order_item.all())

    def __str__(self):
        return f'Order #{self.id}'


class OrderItem(BaseCreatedModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_order_item')
    quantity = models.IntegerField()

    @property
    def total_price(self):
        return self.quantity * self.product.price


