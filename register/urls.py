from django.contrib import admin
from .views import create_participant, create_vehicle
from django.urls import path

urlpatterns = [
    path('creat_part/', create_participant, name='add_part'),
    path('creat_vehi/', create_vehicle, name='add_vehicle'),
]
