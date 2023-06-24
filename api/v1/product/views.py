from api.v1.utilis.get_queries import get_active_category_queryset, get_category_queryset
from .models import Category
from .serializers import (
    CategoryChildrenSerialzer,
    CategoryCreateSerialzier,
    CategoryRetrieveSerialzer,
    ProductCreateSerializer
)
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from api.v1.utilis.custom_responses import (
    params_error_repsonse,
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
        categories = get_active_category_queryset()
        if request.method_name == "category.children":
            category_id = request.query_params.get('category_id')
            if not category_id: return Response(params_error_repsonse())
            categories = categories.filter(parent_id=category_id).order_by("-id")
            serializer = CategoryChildrenSerialzer(categories, many=True)
            return Response(serializer_without_paginator_res(serializer.data))
        else:
            categories = categories.filter(parent__isnull=True)
            serializer = CategoryRetrieveSerialzer(categories, many=True, context = {'lang': request.lang, 'role': request.user.role})
            return Response(serializer_without_paginator_res(serializer.data))
    

    def patch(self, request, *args, **kwargs):
        category_id = request.query_params.get('category_id')
        category = get_active_category_queryset().filter(id=category_id).first()
        if not category: return Response(params_error_repsonse())
        serializer = CategoryCreateSerialzier(data=request.POST, instance=category, partial=True)
        if not serializer.is_valid(): return Response(serializer_error_response(serializer.errors))
        serializer.save()
        return Response(success_response())

    def delete(self, request, *args, **kwargs):
        category_id = request.query_params.get('category_id')
        category = get_active_category_queryset().filter(id=category_id).first()
        if not category: return Response(params_error_repsonse())
        category.is_active = False
        category.is_deleted = True
        category.save()
        return Response(success_response())




class ProductCreateAPi(CustomCreateAPIView, APIView):
    permission_classes = (IsAuthenticated, IsAdmin)
    serializer_class = ProductCreateSerializer
