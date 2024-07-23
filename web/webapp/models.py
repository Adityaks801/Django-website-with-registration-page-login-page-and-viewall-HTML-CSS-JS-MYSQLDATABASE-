from django.db import models

# Create your models here.

   









class Profile(models.Model):
    userid = models.CharField(max_length=30)
    address = models.CharField(max_length=100)  
    mobile = models.CharField(max_length=12)
    email   = models.EmailField(max_length=100)
    gender =models.CharField(max_length=100)
    dob = models.DateField(max_length=100)
class Login(models.Model):
    userid = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
