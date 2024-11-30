from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema

from products.models import Product, Review, Category, SubCategory
from products.serilayzer import (
    ProductListSerializer, ProductCreateSerializer, ReviewCreateSerializer,
    ReviewListSerializer, CategorySerializer, SubCategorySerializer
)
from products.filter import ProductFilter, ReviewFilter, CategoryFilter, SubCategoryFilter

# Create your views here.


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filterset_class = ProductFilter


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer


class ReviewCreateAPIView(APIView):

    @extend_schema(
        request=ReviewCreateSerializer
    )
    def post(self, request, product_id):
        # Mahsulotni topish
        product = get_object_or_404(Product, id=product_id)

        # Serializerni tekshirish
        serializer = ReviewCreateSerializer(data=request.data)
        if serializer.is_valid():
            # Yangi review yaratish
            review = serializer.save(product=product)

            # Mahsulotning reytingini yangilash
            product.update_rating()  # Endi faqat update_rating() chaqiramiz

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewListAPIView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    filterset_class = ReviewFilter


class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter


class SubCategoryCreateAPIView(CreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SubCategoryListAPIView(ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    filterset_class = SubCategoryFilter

