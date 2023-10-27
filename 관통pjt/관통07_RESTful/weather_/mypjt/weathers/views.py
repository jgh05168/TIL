from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.conf import settings
from .serializers import WeatherSerializer
from django.http import JsonResponse
from .models import Weather
# Create your views here.

@api_view(['GET'])
def index(request):
    api_key = settings.API_KEY
    city = 'Seoul, KR'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
    
    response = requests.get(url).json()

    return Response(response)


@api_view(['GET'])
def save_data(request):
    api_key = settings.API_KEY
    city = 'Seoul, KR'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
    
    response = requests.get(url).json()

    for li in response.get('list'):
        save_data = {
            'dt_txt': li.get('dt_txt'),
            'temp': li.get('main').get('temp'),
            'feels_like': li.get('main').get('feels_like'),
        }

        serializer = WeatherSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    return JsonResponse({'message': 'okay'})

@api_view(['GET'])
def list_data(request):
    weathers = Weather.objects.all()
    serializer = WeatherSerializer(weathers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def hot_weathers(request):
    weathers = Weather.objects.all()
    hot_weathers = []
    for weather in weathers:
        tmp = round(weather.temp - 273.15, 2)
        if tmp > 20:
            hot_weathers.append(weather)

    serializer = WeatherSerializer(hot_weathers, many=True)
    return Response(serializer.data)