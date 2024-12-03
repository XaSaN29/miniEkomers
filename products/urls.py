
from django.urls import path, include

from products.views import (
    ProductListAPIView, ProductCreateAPIView, ReviewCreateAPIView, ReviewListAPIView,
    CategoryCreateAPIView, CategoryListAPIView, SubCategoryCreateAPIView, SubCategoryListAPIView
)


urlpatterns = [
    # Product create or list
    path('product-list/', ProductListAPIView.as_view(), name='product_list'),
    path('product-create/', ProductCreateAPIView.as_view(), name='product_create'),
    # Product comment
    path('product-comment-create/', ReviewCreateAPIView.as_view(), name='product_comment_create'),
    path('product-comment-list/', ReviewListAPIView.as_view(), name='product_comment_list'),
    # Product category or subcategory
    path('category-create/', CategoryCreateAPIView.as_view(), name='category_create'),
    path('category-list/', CategoryListAPIView.as_view(), name='category_list'),
    path('subcategory-create/', SubCategoryCreateAPIView.as_view(), name='subcategory_create'),
    path('subcategory-list/', SubCategoryListAPIView.as_view(), name='subcategory_list'),
]