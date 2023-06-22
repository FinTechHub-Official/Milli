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
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class AbstractBaseTitleClass(models.Model):
    title_ln = models.CharField(max_length=255)
    title_kr = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class AbstractDefaultClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.is_active
