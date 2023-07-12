from django.urls import path
from api.v1.product.views.admin_views import (
    CategoryAPi,
    ProductAPi,
    UzumCategory,
    BrandApi,
    CountryApi
)


urlpatterns = [
    path("", ProductAPi.as_view()),
    path("category/", CategoryAPi.as_view()),
    path("country/", CountryApi.as_view()),
    path("brand/", BrandApi.as_view()),
    path("uzum/", UzumCategory.as_view()),
]


