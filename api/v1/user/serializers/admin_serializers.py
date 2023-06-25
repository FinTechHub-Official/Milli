from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import (
    ValidationError
)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        if user.role != 'admin':
            raise ValidationError("Admin not found")
        data['role'] = user.role
        return data
    