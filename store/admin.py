from django.contrib import admin
from .models import (
    ProductTag, Product, ProductComment,
    Cart,
)


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_display_links = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'is_published')
    list_display_links = ('id', 'name')


@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'is_active')
    list_display_links = ('id', 'name')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'created_at', 'quantity')
    list_display_links = ('id', 'product')
