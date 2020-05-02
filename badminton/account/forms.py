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

class inventoryform(ModelForm):
    class Meta:
        model=inventory
        fields = ['item' , 'quantity']

Nums=[
    ('Racket' , 'Racket'),
    ('Shoes','Shoes'),
    ('Grips' ,'Grips'),
    ('Shuttle' , 'Shuttle')
]
class issueform(forms.Form):
    Nums=forms.CharField(widget=forms.RadioSelect(choices=Nums))


class complaint_form(forms.Form):
    Complaint = forms.CharField(widget=forms.Textarea(attrs={"rows":10, "cols":90}))
    

vote=[
    ('Upvote', 'Upvote'),
    ('Downvote','Downvote')
]
class vote_form(forms.Form):
    vote=forms.CharField(widget=forms.RadioSelect(choices=Nums))
    