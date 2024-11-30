from rest_framework import serializers

from carts.models import Cart
from products.models import Product


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'products', 'quantity', 'new_price', 'total_price']
