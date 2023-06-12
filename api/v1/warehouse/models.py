from django.db import models
from api.v1.product.models import Product, ProductPrice


class Warehouse(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, unique=True)
    passport = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.phone_number


class ImportProductToWarehouse(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    import_price = models.PositiveIntegerField(default=0)
    sell_price = models.ForeignKey(ProductPrice, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.product.title_ln
    

class ProductInWarehouse(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.product.title_ln

