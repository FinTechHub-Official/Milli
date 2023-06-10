from .models import Category
from .serializers import (
    CategoryCreateSerialzier,
    CategoryRetrieveSerialzer
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

class CategoryAPi(APIView):

    # @swagger_auto_schema(request_body=CategoryCreateSerialzier)
    def post(self, request, *args, **kwargs):
        serializer = CategoryCreateSerialzier(request)
        if not serializer.is_valid():
            return Response(serializer_error_response(serializer))
        serializer.save()
        return Response(success_response())

    # @swagger_auto_schema(request_body=CategoryRetrieveSerialzer)
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'HTTP-ACCEPR-LANGUAGE',
                openapi.IN_HEADER,
                description='Custom header description',
                type=openapi.TYPE_STRING,
            ),
        ]
    )
    def get(self, request, *args, **kwargs):
        categories = Category.objects.select_related("parent").filter(parent__isnull=True)
        serializer = CategoryRetrieveSerialzer(categories, many=True, context = {'lang': request.lang})
        return Response(serializer_without_paginator_res(serializer))

