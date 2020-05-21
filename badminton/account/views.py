from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, profileform, inventoryform , issueform , complaint_form
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import profile as userProfile
from .models import *
from django.core.mail import send_mail

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

@login_required(login_url='/login/')
def logouts(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url='/login/')
def profile(request):
    prof = request.user.profile
    form = profileform(instance=prof)
    if request.method == "POST":
        form = profileform(request.POST , request.FILES , instance=prof)
        if form.is_valid():
            form.save()
    obj, created = issue_item.objects.get_or_create(user=request.user)
    issued_item="No item issued"
    if created is True:
        issued_item="No items Issued"
    if created==False:
            count_item=obj.count
            if count_item==1:
                    issued_item=obj.itemu
            elif count_item==0:
                    issued_item="No items Issued"
    context={'form':form ,'i':issued_item}
    return render(request , 'account/profile.html',context)


def about(request):
    return render(request , 'account/about.html')

@login_required(login_url='/login/')
def add_inventory(request):
    if request.method == "POST":
        item = request.POST["item"]
        quantity = request.POST["quantity"]
        inven = inventory(item=item,quantity=quantity )
        inven.save()
    invent = inventory.objects.all()
    context = {"invent":invent }
    return render(request , 'account/issue.html',context)

def update_inventory(request):
    inv = request.inventory
    form_i = inventoryform(instance=inv)
    if request.method == "POST":
        form_i = inventoryform(request.POST , request.FILES , instance=prof)
        if form_i.is_valid():
            form_i.save()
    context={'form':form_i}
    return render(request , 'account/update_inven.html',context)

@login_required(login_url='/login/')
def issue(request):
    options = issueform(request.POST)

    if options.is_valid() :
        count_item=0
        obj, created = issue_item.objects.get_or_create(user=request.user)
        if created==False:
            count_item=obj.count
        if count_item==1 :
            messages.error(request , "You already have an issued item")
        else:
            selected= options.cleaned_data.get("Nums")
            inv = inventory.objects.get(item=selected)
            invq=inv.quantity
            if(invq>0):
                invq=invq-1
                newinv= inventory(item=selected, quantity=invq)
                newinv.save()
                names = request.user.profile.name
                rolls=request.user.profile.roll
                entry = issue_item.objects.get(user=request.user )
                entry.itemu=inv
                entry.count=1
                entry.save()
                messages.success(request , "Your application has been submitted")
                '''send_mail(
                    'Issue Application',
                    'Following items is requested by user: '+ names +'\n'+'Roll number: '+str(rolls) +' \n' +str(inv)  ,
                    'ssamarth1201@gmail.com',
                    ['samarth.ss121@gmail.com', '2018288@iiitdmj.ac.in'],
                    fail_silently=False,
                )'''
            elif(invq==0):
                messages.warning(request, "Please Check inventory , Item not available")    
    return render(request , 'account/issue1.html',{'options':options})


def complaints(request):
    if request.method=="POST":
        form = complaint_form(request.POST)
        complaint = request.POST["Complaint"]
        c = complaints_posted(user = request.user , comp = complaint)
        c.save()
        messages.success(request, "Your Complaint has been Successfully registered")
    else:
        form = complaint_form()
    context = {'form':form}
    return render(request , 'account/complaints.html',context)


def blog(request):
    
    context= {
        'posts' : complaints_posted.objects.all()
    }
    return render(request , "account/blog.html" , context)
