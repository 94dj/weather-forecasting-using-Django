from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WeatherViewSet
from .views import get_weather_by_city

urlpatterns = [
    path('weather-by-city/', get_weather_by_city, name='get_weather_by_city'),
]

router = DefaultRouter()
router.register(r'weather', WeatherViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
