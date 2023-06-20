from django.urls import path
from .views import (
    CategoryAPi,
    ProductCreateAPi
)


urlpatterns = [
    path("", ProductCreateAPi.as_view()),
    path("category/", CategoryAPi.as_view()),
]


