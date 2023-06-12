from django.db import models
from api.v1.utilis.abstract_classes import AbstractBaseClass


class Category(AbstractBaseClass):
    icon = models.ImageField(upload_to='product/category/icons/', blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='children')

    def __str__(self) -> str:
        return self.title_ln


class Product(AbstractBaseClass):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    attributes_ln = models.JSONField(blank=True, null=True, default=dict)
    attributes_kr = models.JSONField(blank=True, null=True, default=dict)
    attributes_ru = models.JSONField(blank=True, null=True, default=dict)
    attributes_en = models.JSONField(blank=True, null=True, default=dict)

    def __str__(self) -> str:
        return self.title_ln


class Characteristic(AbstractBaseClass):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.product.title_ln} - {self.title_ln}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='product/images/')

    def __str__(self) -> str:
        return self.product.title_ln


class ProductPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.product.title_ln
