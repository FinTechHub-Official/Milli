from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializers import ProposalSerializer
from api.v1.utilis.custom_responses import (
    success_response,
    serializer_error_response
)


class ProposalApi(APIView):

    @swagger_auto_schema(request_body=ProposalSerializer)
    def post(self, request, *args, **kwargs):
        serializer = ProposalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(success_response())
        return Response(serializer_error_response(serializer.errors))
