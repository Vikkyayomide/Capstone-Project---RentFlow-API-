from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)

urlpatterns = [
    path('', views.property_list, name='property_list'),
    path('', include(router.urls)),
]