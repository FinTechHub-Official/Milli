from django.urls import path
from .views import (
    CategoryAPi,
)


urlpatterns = [
    path("category/", CategoryAPi.as_view()),
]


