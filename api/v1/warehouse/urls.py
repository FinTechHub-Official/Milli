from django.urls import path
from .views import CustomerAPi


urlpatterns = [
    path('customer/', CustomerAPi.as_view()),
]
