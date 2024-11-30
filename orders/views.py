from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from orders.models import Order
from products.models import Product


class OrderCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]




