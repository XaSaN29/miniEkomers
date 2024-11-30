from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter

from products.models import Product, Review, Category, SubCategory


class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    price = filters.RangeFilter(field_name='price')
    subcategory = filters.CharFilter(field_name='subcategory__name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name', 'price', 'subcategory']


class ReviewFilter(filters.FilterSet):
    product = filters.CharFilter(field_name='product__name', lookup_expr='icontains')

    class Meta:
        model = Review
        fields = ['product']


class CategoryFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['name']


class SubCategoryFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = SubCategory
        fields = ['name']
