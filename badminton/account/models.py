from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(null=True,max_length=1000)
    roll = models.IntegerField(null=True)
    phone = models.CharField(null=True,max_length=11)
    profile_pic = models.ImageField(null=True , blank=True)

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
    

    def __str__(self):
        return str(self.user)
    