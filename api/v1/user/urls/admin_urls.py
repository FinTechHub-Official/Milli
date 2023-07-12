from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from api.v1.user.views.admin_views import MyTokenObtainPairView
app_name = 'v1_user_admin_urls'

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
