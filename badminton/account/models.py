from django.db import models
from django.contrib.auth.models import User
from datetime import datetime  
from .choices import *
# Create your models here.


class profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(null=True,max_length=1000)
    pincode = models.IntegerField(null=True)
    phone = models.CharField(null=True,max_length=11)
    profile_pic = models.ImageField(null=True , blank=True)

    def __str__(self):
        return self.name

class product(models.Model):
    name = models.CharField(null=False,max_length=1000)
    product_type = models.CharField(max_length=100 , choices=PRODUCT_CHOICES)
    seller = models.ForeignKey(User , on_delete=models.CASCADE, related_name="seller_user")
    seller_contact = models.CharField(default="123",max_length=100)
    months_old = models.IntegerField()
    city = models.CharField(max_length=100)
    price = models.IntegerField()
    condition = models.CharField(max_length=100 , choices = CONDITION_CHOICES)
    def __str__(self):
        return self.name



class inventory(models.Model):
    item = models.CharField( max_length=100, primary_key=True , unique=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.item

class issue_item(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE, related_name="issue_user")
    itemu = models.ForeignKey(inventory , on_delete=models.CASCADE, null=True)
    count = models.IntegerField(null=True)

    def __str__(self):
        return str(self.user)

class complaints_posted(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name="c_user")
    comp = models.TextField(null = False)
    time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.user)
    