from django.contrib import admin

from .models import (
    ImportToWarehouseCart,
    Warehouse
)


@admin.register(ImportToWarehouseCart)
class ImportToWarehouseCartAdmin(admin.ModelAdmin):
    list_display = ("id", 'warehouse', 'seller', 'created_at', 'is_active', 'is_deleted')


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ("id", 'title', 'is_active', 'is_deleted')
