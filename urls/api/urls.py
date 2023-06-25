from django.urls import path, include

app_name = 'api'

urlpatterns = [
    # path('api/v1/proposal/', include("api.v1.proposal.urls")),
    path('product/', include("api.v1.product.urls.admin_urls")),
    # path('api/v1/user/', include("api.v1.user.urls")),
    # path('api/v1/warehouse/', include("api.v1.warehouse.urls")),
]