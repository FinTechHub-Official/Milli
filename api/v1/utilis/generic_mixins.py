from rest_framework import generics, mixins
from rest_framework.response import Response
from api.v1.utilis.custom_responses import success_response, serializer_error_response
from rest_framework import status


class CustomCreateModelMixin(mixins.CreateModelMixin):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer_error_response(serializer.errors))
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(success_response(), status=status.HTTP_201_CREATED, headers=headers)


class CustomCreateAPIView(CustomCreateModelMixin, generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    