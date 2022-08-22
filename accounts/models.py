from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    phonenumber = models.CharField(max_length=12)
    Admin= models.BooleanField('Admin',default=False)
    Agent = models.BooleanField('Agent',default=True)


    def __str__(self):
        return self.username

