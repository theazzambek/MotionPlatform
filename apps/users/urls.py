from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CustomLoginAPIView, health_check

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Добавляет маршруты для UserViewSet
    path('login/', CustomLoginAPIView.as_view(), name='login'),  # Эндпоинт для логина
    path('health-check/', health_check, name='health-check'),  # Простая проверка состояния
]
