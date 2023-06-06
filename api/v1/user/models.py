from django.contrib.auth.base_user import BaseUserManager
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
    is_stuff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["role"]

    objects = CustomManager()

    def format(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.first_name,
            "phone_number": self.phone_number,
            "role": self.role,
            "is_active": self.is_active,
            "is_stuff": self.is_stuff,
        }

    def __str__(self) -> str:
        return self.phone_number




