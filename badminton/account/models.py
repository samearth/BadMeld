from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(null=True,max_length=1000)
    roll = models.IntegerField(null=True)
    phone = models.CharField(null=True,max_length=11)
    profile_pic = models.ImageField(null=True , blank=True)