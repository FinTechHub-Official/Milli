from django.urls import path
from .views import (
    ImportToWarehouseCartApi,
)


urlpatterns = [
    path("import-cart/", ImportToWarehouseCartApi.as_view()),
]

