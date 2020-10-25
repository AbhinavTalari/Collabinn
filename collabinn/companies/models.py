from django.db import models

# accounts.models.py

from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Email address is a must')
        if not username:
            raise ValueError('User Name is a must')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user	
    def create_superuser(self, email, username, password):
        user = self.create_user(
        	email=self.normalize_email(email),
        	password=password,
        	username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Company(AbstractBaseUser):
    
    email = models.EmailField(verbose_name='email',max_length=255,unique=True)
    company_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    company_uid = models.CharField(max_length=30, unique=True)
    date_of_est = models.DateField(max_length=8,null=True)
    expertise=models.TextField(verbose_name='expertise',max_length=255,null=True)
    interests=models.TextField(max_length=255,verbose_name='interests',null=True)
    

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) 
    is_superuser = models.BooleanField(default=False) 
    #passwords are built in 
   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['company_uid'] 

    objects = UserManager()

    def __str__(self):              
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific  object wise permission?"
       
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to access app with appname `app_label`?"
      
        return True



