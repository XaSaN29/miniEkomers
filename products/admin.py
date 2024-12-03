from django.contrib import admin

from products.models import Category, SubCategory, ProductImage, Product, Review, Tags, Color, Ratio


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(SubCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Ratio)
class RatioAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'id', 'image')


class ProductImageInlabe(admin.StackedInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'price', 'sale_price', 'average_rating')
    list_filter = ('subcategory', 'is_active')
    inlines = [ProductImageInlabe, ]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product',  'id', 'comment', 'rating', 'created_at')

