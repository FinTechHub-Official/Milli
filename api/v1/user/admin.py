from django.contrib import admin

# from api.v1.user.forms import MyUserCreationForm
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", 'first_name', 'phone_number', 'role', 'is_active')
    # form = MyUserCreationForm
    
