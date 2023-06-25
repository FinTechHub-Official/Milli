from django.urls import path
from .views1 import (
    CategoryAPi,
    ProductCreateAPi
)


urlpatterns = [
    path("", ProductCreateAPi.as_view()),
    path("category/", CategoryAPi.as_view()),
]


