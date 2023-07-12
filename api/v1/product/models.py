from django.db import models
from api.v1.utilis.abstract_classes import (
    AbstractBaseClass,
    AbstractBaseTitleClass,
    AbstractDefaultClass
)
from api.v1.user.models import Seller


class Category(AbstractBaseClass):
    """
    Product Category
    """
    icon = models.ImageField(upload_to='product/category/icons/', blank=True, null=True)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True, related_name='children'
    )

    def __str__(self) -> str:
        return self.title_ln


class Brand(AbstractBaseTitleClass):
    """
    Product Brand
    """
    pass


class Country(AbstractBaseTitleClass):
    """
    Country for know Where product made or came
    """
    pass


class Product(AbstractBaseClass):
    """
    Product model
    """
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    attributes_ln = models.JSONField(blank=True, null=True, default=dict)
    attributes_kr = models.JSONField(blank=True, null=True, default=dict)
    attributes_ru = models.JSONField(blank=True, null=True, default=dict)
    attributes_en = models.JSONField(blank=True, null=True, default=dict)

    def __str__(self) -> str:
        return self.title_ln


class CharacterItem(AbstractBaseTitleClass):
    """
    Product character item, for example colors, sizes, memory options
    """
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title_ln


class Characteristic(AbstractDefaultClass):
    """
    Attach character to product
    """
    title = models.ForeignKey(CharacterItem, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='parent_characteristic'
    )

    def __str__(self) -> str:
        return f"{self.title_ln}"


class LinkedCharacteristic(AbstractDefaultClass):
    """
    Connect two characteristic object for giving price, quantity we will use it
    in warehouse or selleing time to know which character of product is changing
    """
    characteristic1 = models.ForeignKey(
        Characteristic, on_delete=models.SET_NULL, null=True, related_name='linked_characteristic1'
    )
    characteristic2 = models.ForeignKey(
        Characteristic, on_delete=models.SET_NULL, null=True, related_name='linked_characteristic2'
    )
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"{self.characteristic1.title.parent.title_ln} - {self.characteristic1.title.parent.title_ln}"


class ProductImage(AbstractDefaultClass):
    """
    Product Image
    """
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    characteristic = models.ForeignKey(LinkedCharacteristic, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='product/images/')

    def __str__(self) -> str:
        return self.product.title_ln
