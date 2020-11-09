from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class MeetingInfo(models.Model):
    company_A=models.CharField(max_length=50)
    company_B=models.CharField(max_length=50)
    venue=models.CharField(max_length=50)
    date=models.DateField()
    security_req=models.BooleanField()

    def __str__(self):              
        return "Meeting between {} and {} at {} on {}. (Where security requirement is: {} )".format(self.company_A,self.company_B,self.venue,self.date,self.security_req)



