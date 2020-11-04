from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from meetings import views

urlpatterns = [
    path("",views.meethome_view,name='meetings_home'),
    path("request",views.request_companies_view,name='request_companies'),
    path("choose",views.choose_view,name='choose-companies'),
]
