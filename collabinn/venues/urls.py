from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from venues import views

urlpatterns = [
    path("",views.venueshome_view,name='venues_home'),
]
