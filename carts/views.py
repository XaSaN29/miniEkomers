from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema

from products.models import Product
from .models import Cart
from .serilayzer import CartSerializer


class CaratListView(ListAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cart.objects.all()


class CartCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, slug):
        user = request.user
        product = get_object_or_404(Product, slug=slug)
        cart = Cart.objects.filter(user=user, products=product).first()
        if cart:
            cart.quantity += 1
            cart.save()
        else:
            cart = Cart.objects.create(
                user=user,
                products=product,
                quantity=1,

            )
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

