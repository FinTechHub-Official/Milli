from rest_framework import serializers
from rest_framework.fields import empty
from .models import Category


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
    description = serializers.CharField(allow_blank=True, default='')

    def __init__(self, *args, **kwargs):
        context = kwargs.pop('context', {})
        super().__init__(*args, **kwargs)
        self.context.update(context)

    class Meta:
        model = Category
        fields = ("id", 'icon', 'title', 'description', 'children')

    def get_children(self, obj):
        serializer = self.__class__(obj.children.all(), many=True, context=self.context)
        return serializer.data

    def to_representation(self, instance):
        res = super().to_representation(instance)
        lang = self.context['lang']
        language_fields = {
            'uz-LN': ('title_ln', 'description_ln'),
            'uz-KR': ('title_kr', 'description_kr'),
            'ru-RU': ('title_ru', 'description_ru'),
            'en-US': ('title_en', 'description_en'),
        }
        title_field, description_field = language_fields.get(lang, ('title', 'description'))
        res['title'] = getattr(instance, title_field, None)
        res['description'] = getattr(instance, description_field, None)
        return res
