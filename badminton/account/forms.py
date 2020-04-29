from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['id','username' , 'email' , 'password1' , 'password2']


class profileform(ModelForm):
    class Meta:
        model= profile
        fields = ['id','name' , 'roll' , 'phone']

