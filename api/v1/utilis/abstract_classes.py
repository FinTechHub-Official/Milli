from django.db import models
from .enums import (
    CharacteristicTitleLn,
    CharacteristicTitleKr,
    CharacteristicTitleRu,
    CharacteristicTitleEn
)

class AbstractDefaultClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self.is_active}"


class AbstractBaseTitleClass(AbstractDefaultClass):
    title_ln = models.CharField(max_length=255)
    title_kr = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)

    class Meta:
        abstract = True


class AbstractBaseClass(AbstractBaseTitleClass):
    description_ln = models.CharField(max_length=300, blank=True, null=True)
    description_kr = models.CharField(max_length=300, blank=True, null=True)
    description_ru = models.CharField(max_length=300, blank=True, null=True)
    description_en = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        abstract = True
