from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from products.models import Product, Review, Category, SubCategory


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category']


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'subcategories']


class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'quantity', 'price', 'subcategory']


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'quantity', 'price', 'average_rating', 'subcategory']


class ReviewCreateSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Review
        fields = ['id', 'product_id', 'rating', 'comment', 'created_at']


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['product', 'comment', 'rating']

