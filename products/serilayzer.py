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
        fields = ['id', 'name', 'description', 'quantity', 'price', 'subcategory']


class ReviewCreateSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Review
        fields = ['id', 'product_id', 'rating', 'comment', 'created_at']
        # extra_kwargs = {
        #     'comment': {'required': False, 'allow_blank': True, 'default': ''}
        # }

    def create(self, validated_data):
        product = get_object_or_404(Product, id=validated_data['product_id'])
        validated_data['product'] = product
        return super().create(validated_data)


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['product', 'comment', 'rating']

