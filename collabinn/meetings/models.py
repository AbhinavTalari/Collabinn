from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class MeetingInfo(models.Model):
    company_A=models.CharField(max_length=50)
    company_B=models.CharField(max_length=50)
    venue=models.CharField(max_length=50)
    date=models.DateField()
    security_req=models.BooleanField()



