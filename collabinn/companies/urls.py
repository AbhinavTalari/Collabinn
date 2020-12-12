"""collabinn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from companies import views

urlpatterns = [
    path('',views.renderhome,name='home'),
     path('login', auth_views.LoginView.as_view(template_name='companies/login.html'),name='login'),
     path('logout',views.logout_view,name='logout'),
     path('register',views.register_view,name='register'),
     path('companylist',views.list_companies_view,name='companylist'),
     path('accept/<int:id>',views.invite_accept,name='accept'),
      path('request/<int:id>',views.invite_request,name='request'),
     path('invites',views.invites_view,name='invites'),
     path('outgoing',views.outgoing_invites_view,name='outgoing'),
     path('profile',views.render_profile,name='profile'),
     path('meetings',views.meetings,name='meetings'),
     path('bookhotels',views.bookhotels,name='hotels')
]
