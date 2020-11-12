from django.urls import path,include
from . import views

urlpatterns = [
    path('meetingdata',views.meeting_data_list_view,name='meeting_data_list_view'),
    
]