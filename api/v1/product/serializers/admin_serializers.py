from rest_framework import serializers
from ..models import Brand, Category, Characteristic, Country, Product
from django.db import transaction
import datetime


class CategoryCreateSerialzier(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            "id", 'title_ln', 'title_kr', 'title_ru', 'title_en','parent'
        )


class CategoryRetrieveSerialzer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    title = serializers.CharField(allow_blank=True, default='')

    def __init__(self, *args, **kwargs):
        context = kwargs.pop('context', {})
        super().__init__(*args, **kwargs)
        self.context.update(context)

    class Meta:
        model = Category
        fields = ("id", 'icon', 'title', 'children')

    def get_children(self, obj):
        serializer = self.__class__(obj.children.all(), many=True, context=self.context)
        return serializer.data

    def to_representation(self, instance):
        res = super().to_representation(instance)
        lang = self.context['lang']
        role = self.context.get('role')
        if role == 'admin':
            res['title'] = {
                'title_ln': instance.title_ln,
                'title_kr': instance.title_kr,
                'title_ru': instance.title_ru,
                'title_en': instance.title_en,
            }
            return res
        else:
            language_fields = {
                'uz-LN': ('title_ln',),
                'uz-KR': ('title_kr',),
                'ru-RU': ('title_ru',),
                'en-US': ('title_en',),
            }
            title_field = language_fields.get(lang, ('title',))
            res['title'] = getattr(instance, title_field[0], None)
            return res


class CategoryChildrenSerialzer(serializers.ModelSerializer):
    title = serializers.CharField(allow_blank=True, default='')

    class Meta:
        model = Category
        fields = ("id", 'icon', 'title')

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['title'] = {
            'title_ln': instance.title_ln,
            'title_kr': instance.title_kr,
            'title_ru': instance.title_ru,
            'title_en': instance.title_en,
        }
        return res



class ProductCreateSerializer(serializers.ModelSerializer):
    # characteristic = serializers.ListField()
    # images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'seller', 'category', 'country', 'brand', 
            'title_ln', 'title_kr', 'title_ru', 'title_en',
            'description_ln', 'description_kr', 'description_ru', 'description_en',
            'attributes_ln', 'attributes_kr', 'attributes_ru', 'attributes_en',
            #'characteristic', # 'images'
        )
        extra_kwargs = {
            "seller": {"allow_null": False, "required": True},
            "category": {"allow_null": False, "required": True},
            "country": {"allow_null": False, "required": True},
            "brand": {"allow_null": False, "required": True},
            "title_ln": {"allow_null": False, "required": True},
            "title_kr": {"allow_null": False, "required": True},
            "title_ru": {"allow_null": False, "required": True},
            "title_en": {"allow_null": False, "required": True},
            "description_ln": {"allow_null": False, "required": True},
            "description_kr": {"allow_null": False, "required": True},
            "description_ru": {"allow_null": False, "required": True},
            "description_en": {"allow_null": False, "required": True},
        }



class ProductGetSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'created_at', 'seller',
                   'category')

    def get_title(self, obj):
        return {
            'ln': obj.title_ln,
            'kr': obj.title_kr,
            'ru': obj.title_ru,
            'en': obj.title_en,
        }
    
    def to_representation(self, instance):
        res = super().to_representation(instance)
        if res.get("seller"):
            res['seller'] = {
                'id': instance.seller.id,
                'first_name': instance.seller.first_name,
                'phone_number': instance.seller.phone_number,
            }
        if res.get('category'):
            res['category'] = {
                'id': instance.category.id,
                'title': {
                    'ln': instance.category.title_ln,
                    'kr': instance.category.title_kr,
                    'ru': instance.category.title_ru,
                    'en': instance.category.title_en,
                }
            }
        return res


class ProductDetailSerialzier(serializers.ModelSerializer):
    characteristics = serializers.SerializerMethodField()
    attributes = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id', 'title', 'created_at', 'seller', 'category', 'attributes', 'characteristics'
        )
    
    def get_title(self, obj):
        return {
            'ln': obj.title_ln,
            'kr': obj.title_kr,
            'ru': obj.title_ru,
            'en': obj.title_en,
        }
    
    def get_attributes(self, obj):
        return {
            'ln': obj.attributes_ln,
            'kr': obj.attributes_kr,
            'ru': obj.attributes_ru,
            'en': obj.attributes_en,
        }
    
    def get_characteristics(self, obj):
        pass

    def to_representation(self, instance):
        res = super().to_representation(instance)
        if res.get("seller"):
            res['seller'] = {
                'id': instance.seller.id,
                'first_name': instance.seller.first_name,
                'phone_number': instance.seller.phone_number,
            }
        if res.get('category'):
            res['category'] = {
                'id': instance.category.id,
                'title': {
                    'ln': instance.category.title_ln,
                    'kr': instance.category.title_kr,
                    'ru': instance.category.title_ru,
                    'en': instance.category.title_en,
                }
            }
        return res


class BrandSerialzier(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = Brand
        fields = ("id", 'title')

    def get_title(self, instance):
        return instance.title_ln


class CountrySerialzier(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = Country
        fields = ("id", 'title')

    def get_title(self, instance):
        return instance.title_ln