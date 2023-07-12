from django.contrib import admin
from .models import (
    Category,
    Brand,
    Country,
    Product,
    CharacterItem,
    Characteristic,
    LinkedCharacteristic,
    ProductImage
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_ln', 'parent', 'created_at')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", 'title_ln', 'created_at', 'is_active', 'is_deleted')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("id", 'title_ln', 'created_at', 'is_active', 'is_deleted')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title_ln', 'category', 'seller', 'is_deleted', 'is_active')


@admin.register(CharacterItem)
class CharacterItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_ln', 'value', 'parent', 'created_at', 'is_deleted', 'is_active')


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'product', 'parent', 'created_at', 'is_deleted', 'is_active')


@admin.register(LinkedCharacteristic)
class LinkedCharacteristicAdmin(admin.ModelAdmin):
    list_display = ('id', 'characteristic1', 'characteristic2', 'parent', 'created_at', 'is_deleted', 'is_active')


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'characteristic', 'created_at', 'is_deleted', 'is_active')
