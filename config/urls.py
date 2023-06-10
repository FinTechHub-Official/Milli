from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


# drf_yasg code starts here
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Milli API",
        default_version='v1',
        description="Welcome to the world of Milli",
        terms_of_service="https://www.milli.uz",
        contact=openapi.Contact(email="info.kamalov@gmail.com"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)
# ends here

urlpatterns = [
    path('milli-admin/', admin.site.urls),

    # SWAGGER
    path('milli-schema/',schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('milli-api-doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('milli-redoc/', schema_view.with_ui('redoc', cache_timeout=0),name='schema-redoc'),

    # API V1
    path('api/v1/proposal/', include("api.v1.proposal.urls")),
    path('api/v1/product/', include("api.v1.product.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
