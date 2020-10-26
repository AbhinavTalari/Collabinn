from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from meetings import views

urlpatterns = [
    path("",views.meethome,name='meetings_home'),
]
