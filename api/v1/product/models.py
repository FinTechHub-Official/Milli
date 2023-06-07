from django.db import models


class Category(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    description_uz = models.CharField(max_length=300, blank=True, null=True)
    description_ru = models.CharField(max_length=300, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return self.title


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