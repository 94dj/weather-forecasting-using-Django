from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Weather
from .serializers import WeatherSerializer

import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings

@api_view(['POST'])
def get_weather_by_city(request):
    city = request.data.get('city')
    if not city:
        return Response({'error': 'City name is required'}, status=400)

    api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
    response = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    )
    if response.status_code != 200:
        return Response({'error': 'City not found'}, status=404)

    data = response.json()
    weather_data = {
        'city': city,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description']
    }

    # Optionally save the weather data to the database
    # weather = Weather.objects.create(**weather_data)

    return Response(weather_data)


class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
