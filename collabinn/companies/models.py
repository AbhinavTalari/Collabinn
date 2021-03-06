from django.db import models

# accounts.models.py

from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class UserManager(BaseUserManager):
    def create_user(self, email, company_uid, password=None):
        if not email:
            raise ValueError('Email address is a must')
        if not company_uid:
            raise ValueError('User Name is a must')
        user = self.model(
            email=self.normalize_email(email),
            company_uid=company_uid,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user	
    def create_superuser(self, email, company_uid, password):
        user = self.create_user(
        	email=self.normalize_email(email),
        	password=password,
        	company_uid=company_uid,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
    

class Company(AbstractBaseUser):
    
    email = models.EmailField(verbose_name='email',max_length=100,unique=True)
    company_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    company_uid = models.CharField(max_length=30, unique=True)
    date_of_est = models.DateField(max_length=8,null=True)
    expertise=models.TextField(verbose_name='expertise',max_length=100,null=True)
    interests=models.TextField(max_length=100,verbose_name='interests',null=True)
    relationships = models.ManyToManyField('self', through='CollabRequest',symmetrical=False,related_name='related_to+')
    
    

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) 
    is_superuser = models.BooleanField(default=False) 
    #passwords are built in 
    
    

   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['company_uid'] 

    objects = UserManager()

    def __str__(self):              
        return self.company_uid

    def has_perm(self, perm, obj=None):
        "Does the user have a specific  object wise permission?"
       
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to access app with appname `app_label`?"
      
        return True
    
    
        
    def add_relationship(self, person, status,date,location, symm=True):
        relationship, created = CollabRequest.objects.get_or_create(
        from_user=self,
        to_user=person,
        status=status,
        meeting_date=date,
        meeting_location=location)
        # if symm:
        #     person.add_relationship(self, status,date,location, False)
        # person.save()
        # self.save()    
        relationship.save()
        return relationship

    def remove_relationship(self, person, status, symm=True):
        CollabRequest.objects.filter(
        from_person=self,
        to_person=person,
        status=status).delete()
        if symm:
        # avoid recursion by passing `symm=False`
            person.remove_relationship(self, status, False)
            
    def get_relationships(self, status):
        # return self.relationships.filter(
        # from_company__status=status,
        # to_company__from_person=self)
        return CollabRequest.objects.filter(to_user=self, status=status) or \
                CollabRequest.objects.filter(from_user=self, status=status)
        
        
        
    
    
RELATIONSHIP_REQUESTED = 1
RELATIONSHIP_BLOCKED = 2
RELATIONSHIP_ACCEPTED =3
RELATIONSHIP_SENT=4
RELATIONSHIP_STATUSES = (
(RELATIONSHIP_REQUESTED, 'Requested'),
(RELATIONSHIP_BLOCKED, 'Blocked'),
(RELATIONSHIP_ACCEPTED,'Accepted'),
(RELATIONSHIP_SENT,'Sent')
)  



class CollabRequest(models.Model):
    to_user=models.ForeignKey(Company,related_name='to_company',on_delete=models.CASCADE)
    from_user=models.ForeignKey(Company,related_name='from_company',on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=RELATIONSHIP_STATUSES,null=True)
    meeting_date=models.DateField(null=True)
    meeting_location=models.CharField(max_length=50,null=True)
    
    def __str__ (self):
        # return "Collab Request From {},to {}".format(self.to_user.company_name,self.from_user.company_name)
        return "Collab Request From {},to {}".format(self.from_user.company_name,self.to_user.company_name)
    

class Company_Profile(models.Model):
    user=models.OneToOneField(Company, verbose_name=("Company Profile"), on_delete=models.CASCADE)
    company_logo=models.ImageField(upload_to='profile_logos', height_field=None, width_field=None, max_length=None,blank=True, null=True)
    


