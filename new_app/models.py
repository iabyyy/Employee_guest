from django.contrib.auth.models import AbstractUser
from django.db import models

class Login(AbstractUser):
    is_contractor = models.BooleanField(default=False)
    is_guest = models.BooleanField(default=False)

class Contractor(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='contractor_profile')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name

class Guest(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='guest_profile')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name

class PostJob(models.Model):
    contractor = models.ForeignKey(Contractor, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.TextField()
    description = models.TextField()
    date = models.DateField(auto_now=True)
