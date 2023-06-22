from django.contrib import admin
from .models import (
    Category,
    Product,
    Characteristic
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_ln', 'parent', 'created_at')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_ln', 'category', 'seller', 'is_deleted', 'is_active')


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_ln', 'product', 'parent', 'is_deleted', 'is_active')