from rest_framework import serializers
from rest_framework.fields import empty
from .models import Category, Characteristic, Product
from django.db import transaction
import datetime


class CategoryCreateSerialzier(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            "id", 'title_ln', 'title_kr', 'title_ru', 'title_en' 'description_ln',
            'description_kr', 'description_ru', 'description_en', 'parent'
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
            title_field, description_field = language_fields.get(lang, ('title',))
            res['title'] = getattr(instance, title_field, None)
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
    characteristic = serializers.ListField()
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'seller', 'category', 'title_ln', 'title_kr', 'title_ru', 'title_en',
            'description_ln', 'description_kr', 'description_ru', 'description_en',
            'attributes_ln', 'attributes_kr', 'attributes_ru', 'attributes_en',
            'characteristic', 'images'
        )
    
    def create_characteristic(self, product_id, characteristics, parent_id=None):
        with transaction.atomic():
            for character in characteristics:
                parent_character = Characteristic(
                    product_id=product_id,
                    parent_id=parent_id,
                    title_ln=character.get('title_ln'),
                    title_kr=character.get('title_kr'),
                    title_ru=character.get('title_ru'),
                    title_en=character.get('title_en')
                )
                parent_character.save()
                if character.get("values"):
                    self.create_characteristic(product_id, character.get("values"), parent_character.id)

    # def save_images(self, images, product_id):
    #     product_images = []
    #     for file in images:
    #         f_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    #         file_name = f"{f_time}_{file.name}"
    #         saved_file_path = os.path.join('media', 'sourcing', 'comment', 'files', file_name)
    #         os.makedirs(os.path.dirname(saved_file_path), exist_ok=True)
    #         with open(saved_file_path, 'wb') as destination:
    #             for chunk in file.chunks():
    #                 destination.write(chunk)
    #         comment_files.append(
    #             SourcingCommentFile(
    #                 comment_id=comment_id,
    #                 creator_id=user_id,
    #                 uploaded_file=saved_file_path
    #             )
    #         )
    #     SourcingCommentFile.objects.bulk_create(comment_files)

    def create(self, validated_data):
        res = super().create(validated_data)
        characteristics = validated_data.get('characteristic')
        images = validated_data.get('images')
        if characteristics:
            self.create_characteristic(res.id, characteristics)
        if images:
            pass
        return res
    
