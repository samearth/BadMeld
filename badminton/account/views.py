from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, profileform
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import profile as userProfile
# Create your views here.

def index(request):
    return render(request,'account/index.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        if(request.method == "POST"):
            form=CreateUserForm(request.POST)
            pform = profileform(request.POST)
            if form.is_valid() and pform.is_valid():
                user = form.save()
                userprofile = userProfile.objects.filter(user = user).first()
                userprofile.name= pform.cleaned_data['name']
                userprofile.roll = pform.cleaned_data["roll"]
                userprofile.phone = pform.cleaned_data["phone"]
                userprofile.save()
                username=form.cleaned_data.get('username')
                messages.success(request, 'Account was created for '+ username)
                return redirect('/login')
        else:
            form = CreateUserForm()
            pform = profileform()

    context = {'form':form , 'pform':pform}
    return render(request , 'account/register.html',context)


def login(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        if request.method =='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username , password=password)

            if user is not None:
                auth_login(request,user)
                return redirect('/home/')
            else:
                messages.info(request , "Username or Password incorrect")
        context={}
        return render(request, 'account/login.html',context)

@login_required(login_url='/login/')
def home(request):
    return render(request , 'account/home.html')

def logouts(request):
    logout(request)
    return redirect('/login/')

def profile(request):
    prof = request.user.profile
    form = profileform(instance=prof)

    if request.method == "POST":
        form = profileform(request.POST , request.FILES , instance=prof)
        if form.is_valid():
            form.save()


    context={'form':form}
    return render(request , 'account/profile.html',context)


def about(request):
    return render(request , 'account/about.html')