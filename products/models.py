from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg
from django.utils.text import slugify
# Create your models here.


class BaseCreatedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseCreatedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        # print(self.slug)
        a = 1
        while Category.objects.filter(slug=self.slug).exists():
            self.slug += f'{self.slug} + {a}'

        super().save(*args, force_insert=force_insert, force_update=force_update, using=using,
                     update_fields=update_fields)

    def __str__(self):
        return self.name


class SubCategory(BaseCreatedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        a = 1
        while SubCategory.objects.filter(slug=self.slug).exists():
            self.slug += f'{self.slug} + {a}'

        super().save(*args, force_insert=force_insert, force_update=force_update, using=using,
                     update_fields=update_fields)

    def __str__(self):
        return self.name


class Tags(BaseCreatedModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Color(BaseCreatedModel):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Ratio(BaseCreatedModel):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Product(BaseCreatedModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='product')
    is_active = models.BooleanField(default=True)
    tage = models.ManyToManyField(Tags)
    color = models.ManyToManyField(Color)
    ratio = models.ManyToManyField(Ratio)
    sale = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    rating = models.FloatField(default=0.0, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        a = 1
        while Product.objects.filter(slug=self.slug).exists():
            self.slug += f'{self.slug} + {a}'

        super().save(*args, force_insert=force_insert, force_update=force_update, using=using,
                     update_fields=update_fields)

    @property
    def sale_price(self):
        return self.price - (self.price * self.sale) / 100



class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.product.name


class Review(models.Model):
    class Rating_chois(models.TextChoices):
        One = '1'
        Two = '2'
        Three = '3'
        Four = '4'
        Five = '5'
    comment = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.TextField(choices=Rating_chois)
    created_at = models.DateTimeField(auto_now_add=True)


