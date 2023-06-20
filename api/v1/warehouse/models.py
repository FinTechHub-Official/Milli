from django.db import models
from api.v1.product.models import (
    Product,
    Characteristic,
)
from api.v1.utilis.abstract_classes import AbstractDefaultClass


class Warehouse(AbstractDefaultClass):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.title


class Customer(AbstractDefaultClass):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, unique=True)
    passport = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.phone_number


class ImportToWarehouseCart(AbstractDefaultClass):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)


class ImportProductToWarehouse(AbstractDefaultClass):
    import_to_warehouse_cart = models.ForeignKey(ImportToWarehouseCart, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.product.title_ln


class ProductInWarehouse(AbstractDefaultClass):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return self.product.title_ln


class ImportPriceProductInWarehouse(AbstractDefaultClass):
    import_product_to_warehouse = models.ForeignKey(ImportProductToWarehouse, on_delete=models.SET_NULL, null=True)
    product_in_warehouse = models.ForeignKey(ProductInWarehouse, on_delete=models.SET_NULL, null=True)
    characteristic = models.ForeignKey(Characteristic, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=4)


class SellPriceProductInWarehouse(AbstractDefaultClass):
    product_in_warehouse = models.ForeignKey(ProductInWarehouse, on_delete=models.SET_NULL, null=True)
    characteristic = models.ForeignKey(Characteristic, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=4)


class ImportQuantityProductInWarehouse(AbstractDefaultClass):
    import_product_to_warehouse = models.ForeignKey(ImportProductToWarehouse, on_delete=models.SET_NULL, null=True)
    product_in_warehouse = models.ForeignKey(ProductInWarehouse, on_delete=models.SET_NULL, null=True)
    characteristic = models.ForeignKey(Characteristic, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.product_in_warehouse.product.title_ln}, qty: {self.quantity}"


class QuantityProductInWarehouse(AbstractDefaultClass):
    product_in_warehouse = models.ForeignKey(ProductInWarehouse, on_delete=models.SET_NULL, null=True)
    characteristic = models.ForeignKey(Characteristic, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.product_in_warehouse.product.title_ln}, qty: {self.quantity}"


    