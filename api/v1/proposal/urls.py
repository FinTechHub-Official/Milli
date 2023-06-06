from django.urls import path
from .views import ProposalApi


urlpatterns = [
    path("", ProposalApi.as_view()),
]

