from django.urls import path
from api.v1.product.views.admin_views import (
    CategoryAPi,
    ProductCreateAPi
)


urlpatterns = [
    path("", ProductCreateAPi.as_view()),
    path("category/", CategoryAPi.as_view()),
]


