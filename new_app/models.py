from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_guest = models.BooleanField(default=False)


class Employee(models.Model):
    User = models.ForeignKey(Login,on_delete=models.CASCADE,related_name='employee')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name


class Guest(models.Model):
    User = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='guest')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name

