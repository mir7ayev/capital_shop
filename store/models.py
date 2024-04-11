from django.db import models
from config.base_models import BaseModel
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    (1, 'MEN'),
    (2, 'WOMEN'),
    (3, 'BABY')
)


class ProductTag(BaseModel):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=120)
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=1)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    price = models.FloatField()
    discount = models.IntegerField(blank=True, null=True)
    price_with_discount = models.FloatField(blank=True, null=True)

    image = models.ImageField(upload_to='store/products/')
    tags = models.ManyToManyField(ProductTag)
    description = RichTextField()

    is_published = models.BooleanField(default=True)
    is_advertised = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.price_with_discount = self.price * (1 - self.discount / 100)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductComment(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=120)
    message = models.TextField()

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Cart(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.price_with_discount
