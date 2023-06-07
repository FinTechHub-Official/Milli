from rest_framework import serializers
from rest_framework.fields import empty
from .models import Category


class CategoryCreateSerialzier(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ("id", 'title_uz', 'title_ru', 'description_uz', 'description_ru', 'parent')

