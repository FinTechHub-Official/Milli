from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from api.v1.user.enums import UserRole
from api.v1.user.managers import CustomManager


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, unique=True)
    role = models.CharField(max_length=6, choices=UserRole.choices())
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["role"]

    objects = CustomManager()

    def __str__(self) -> str:
        return self.phone_number
    


