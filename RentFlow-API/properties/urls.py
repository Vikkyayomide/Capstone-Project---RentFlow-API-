from django.urls import path
from . import views

urlpatterns = [
    path('', views.property_list, name='property_list'),
    path('<int:property_id>/', views.property_detail, name='property_detail'),
    path('search/', views.property_search, name='property_search'),
]