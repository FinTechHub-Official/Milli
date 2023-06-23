from django.db import models
from api.v1.utilis.abstract_classes import (
    AbstractBaseClass,
    AbstractBaseTitleClass,
    AbstractDefaultClass
)
from api.v1.user.models import Seller


class Category(AbstractBaseClass):
    icon = models.ImageField(upload_to='product/category/icons/', blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='children')

    def __str__(self) -> str:
        return self.title_ln


class Product(AbstractBaseClass):
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    attributes_ln = models.JSONField(blank=True, null=True, default=dict)
    attributes_kr = models.JSONField(blank=True, null=True, default=dict)
    attributes_ru = models.JSONField(blank=True, null=True, default=dict)
    attributes_en = models.JSONField(blank=True, null=True, default=dict)

    def __str__(self) -> str:
        return self.title_ln


class Characteristic(AbstractBaseTitleClass):
    is_title = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='parent_characteristic'
    )

    def __str__(self) -> str:
        return f"{self.title_ln}"


class ProductImage(AbstractDefaultClass):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    characteristic = models.ForeignKey(Characteristic, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='product/images/')

    def __str__(self) -> str:
        return self.product.title_ln


