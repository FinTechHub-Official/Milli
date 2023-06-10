from django.db import models


class AbstractBaseClass(models.Model):
    title_ln = models.CharField(max_length=255)
    title_kr = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)

    description_ln = models.CharField(max_length=300, blank=True, null=True)
    description_kr = models.CharField(max_length=300, blank=True, null=True)
    description_ru = models.CharField(max_length=300, blank=True, null=True)
    description_en = models.CharField(max_length=300, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
