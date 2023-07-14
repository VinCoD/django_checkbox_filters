from django.urls import path
from .views import filter_restaurants

urlpatterns = [
    path('restaurants/', filter_restaurants, name='filter_restaurants'),
]
