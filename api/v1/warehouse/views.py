from rest_framework.views import APIView

from api.v1.utilis.custom_responses import (
    serializer_error_response,
    success_response
)
from api.v1.utilis.permissions import (
    IsAdmin,
)
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomerSerialzier
from rest_framework.response import Response


class ImportToWarehouseApi(APIView):
    # permission_classes = ()

    def post(self, request, *args, **kwargs):
        pass


class CustomerAPi(APIView):
    permission_classes = (IsAuthenticated, IsAdmin)

    def post(self, request, *args, **kwargs):
        serializer = CustomerSerialzier(data=request.data)
        if not serializer.is_valid():
            return Response(serializer_error_response(serializer.errors))
        serializer.save()
        return Response(success_response())
    
    



