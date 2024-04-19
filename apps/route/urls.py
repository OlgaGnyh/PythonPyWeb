from django.urls import include
from django.urls import path
from .views import RoutesViewSet, RoutesGenericAPIView
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('routes/', RoutesGenericAPIView.as_view(), name='routes-list'),
    path('routes/<int:pk>/', RoutesGenericAPIView.as_view(), name='routes-detail'),
    ]

