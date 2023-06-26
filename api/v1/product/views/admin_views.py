from api.v1.utilis.get_queries import (
    get_active_category_queryset,
    get_category_queryset,
    get_active_product_queryset
)
from rest_framework.pagination import PageNumberPagination
from api.v1.product.serializers.admin_serializers import (
    CategoryChildrenSerialzer,
    CategoryCreateSerialzier,
    ProductCreateSerializer,
    ProductDetailSerialzier,
    ProductGetSerializer
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


class ProductAPi(CustomCreateAPIView, APIView):
    """Product create for seller"""
    permission_classes = (IsAuthenticated, IsAdmin)
    serializer_class = ProductCreateSerializer
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        queryset = get_active_product_queryset()
        product_id = request.query_params.get('product_id')
        if not product_id:
            paginated_queryset = self.paginate_queryset(queryset)  # Paginate the queryset
            serializer = ProductGetSerializer(paginated_queryset, many=True)
            paginated_res = self.get_paginated_response(serializer.data)
            return paginated_res
        product = queryset.filter(id=product_id).first()
        serializer = ProductDetailSerialzier(product)
        return Response(serializer_without_paginator_res(serializer.data))


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
        parent_id = request.query_params.get('parent_id')
        if parent_id:
            parent =  categories.filter(id=parent_id).first()
            categories = categories.filter(parent_id=parent_id).order_by("-id")
            serializer = CategoryChildrenSerialzer(categories, many=True)
            return Response({
                'status': True,
                'data': serializer.data,
                'parent': {
                    'id': parent.id,
                    'title_ln': parent.title_ln,
                    'title_kr': parent.title_kr,
                    'title_ru': parent.title_ru,
                    'title_en': parent.title_en
                }
            })
        else:
            categories = categories.filter(parent__isnull=True)
            serializer = CategoryChildrenSerialzer(categories, many=True)
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
