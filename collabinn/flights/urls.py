from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("",views.home_view,name='flight_home'),
    path("contact",views.contact,name='flight_contact'),
    path("data",views.DisplayData,name='DisplayData'),
    path("weather",views.weather,name='weather'),
]
