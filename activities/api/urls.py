from django.urls import path, include
from rest_framework.routers import DefaultRouter

from activities.api.api_views import ArtActivityViewSet

app_name = 'activities'

routers = DefaultRouter()
routers.register(r'activities', ArtActivityViewSet, basename='activities')

urlpatterns = [
    path("", include(routers.urls)),
]
