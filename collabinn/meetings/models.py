from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class MeetingInfo(models.Model):
    company_A=models.CharField(max_length=50,default='')
    company_B=models.CharField(max_length=50,default='')
    venue=models.CharField(max_length=50,default='')
    date=models.DateField()
    security_req=models.BooleanField(default='False')



