from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PotholeEventViewSet, dashboard

router = DefaultRouter()
router.register(r'potholes', PotholeEventViewSet, basename='pothole')

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', dashboard, name='dashboard'),
]