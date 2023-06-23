from .models import Category
from .serializers import (
    CategoryCreateSerialzier,
    CategoryRetrieveSerialzer,
    ProductCreateSerializer
)
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from api.v1.utilis.custom_responses import (
    serializer_error_response,
    serializer_without_paginator_res,
    success_response
)
from rest_framework.permissions import IsAuthenticated
from api.v1.utilis.permissions import IsAdmin
from api.v1.utilis.generic_mixins import CustomCreateAPIView


class CategoryAPi(CustomCreateAPIView, APIView):
    permission_classes = (IsAuthenticated, IsAdmin)
    serializer_class = CategoryCreateSerialzier

    # @swagger_auto_schema(request_body=CategoryRetrieveSerialzer)
    @swagger_auto_schema(manual_parameters=[openapi.Parameter(
                'HTTP-ACCEPR-LANGUAGE',
                openapi.IN_HEADER,
                description='Custom header description',
                type=openapi.TYPE_STRING,
            ),])
    def get(self, request, *args, **kwargs):
        categories = Category.objects.select_related("parent").filter(parent__isnull=True)
        serializer = CategoryRetrieveSerialzer(categories, many=True, context = {'lang': request.lang})
        return Response(serializer_without_paginator_res(serializer.data))
    

    def patch(self, request, *args, **kwargs):
        category_id = request.query_params.get('category_id')
        if not category_id:
            return Response({})
        category = Category.objects.filter(id=category_id).first()
        if not category:
            return Response({})
        serializer = CategoryCreateSerialzier(data=request.POST, instance=category)
        if not serializer.is_valid():
            return Response(serializer_error_response(serializer.errors))
        serializer.save()
        return Response(success_response())

    def delete(self, request, *args, **kwargs):
        category_id = request.query_params.get('category_id')
        if not category_id:
            return Response({})
        category = Category.objects.filter(id=category_id).first()
        if not category:
            return Response({})
        category.is_active = False
        category.is_deleted = True
        category.save()
        return Response(success_response())


class ProductCreateAPi(CustomCreateAPIView, APIView):
    permission_classes = (IsAuthenticated, IsAdmin)
    serializer_class = ProductCreateSerializer
