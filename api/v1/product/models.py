from django.db import models
from api.v1.utilis.abstract_classes import AbstractBaseClass


class Category(AbstractBaseClass):
    icon = models.ImageField(upload_to='product/category/icons/', blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='children')

    def __str__(self) -> str:
        return self.title_ln


# class Product(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
#     title = models.CharField(max_length=255)
#     title_ru = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     description_ru = models.TextField(blank=True, null=True)
#     attributes = models.JSONField(blank=True, null=True, default=dict)
#     attributes_ru = models.JSONField(blank=True, null=True, default=dict)

#     def __str__(self) -> str:
#         return self.title


# class Characteristic(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
#     title = models.CharField(max_length=255)

#     def __str__(self) -> str:
#         return f"{self.product.title} - {self.title}"


# class CharacteristicItem(models.Model):
#     characteristic = models.ForeignKey(Characteristic, on_delete=models.SET_NULL, null=True)
#     title = models.CharField(max_length=255)
#     value = models.CharField(max_length=255)

#     def __str__(self) -> str:
#         return self.title