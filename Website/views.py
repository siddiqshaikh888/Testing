from django.http import request
from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime
from Website.models import register
from django.contrib import messages
from django.forms import inlineformset_factory
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from Website.models import Website
from .models import Selldata


# Create your views here.
def index(request):
    return render(request, 'index.html')

def websitedetail(request):
    if request.method == "POST":
          name = request.POST.get('name')
          email = request.POST.get('email')
          phone = request.POST.get('phone')
          message = request.POST.get('message')
          websitedetail = Website(name=name, email=email, phone=phone, message=message)
          websitedetail.save()
          messages.success(request, 'Your message has been sent!')
    return render(request, 'websitedetail.html')

def marketplace(request):
    if request.method == "POST":
          name = request.POST.get('name')
          email = request.POST.get('email')
          phone = request.POST.get('phone')
          message = request.POST.get('message')
          websitedetail = Website(name=name, email=email, phone=phone, message=message)
          websitedetail.save()
          messages.success(request, 'Your message has been sent!')
    return render(request, 'marketplace.html')

def sell(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        sell = Selldata(name=name, email=email, phone=phone, country=country)
        sell.save()
    return render(request,'sell.html')

def sell2(request):
    return render(request,'sell2.html')    

def selltype(request):   
    return render(request, 'selltype.html')

def sellwebsite(request):   
    return render(request, 'sellwebsite1.html')
 
def login(request): 
    if request.method== 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('/')

    else:
        return render(request,'login.html')    

def register(request):
    if request.method== 'POST':
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
    
        if password1==password2:
            if User.objects.filter(email=email).exists():
                print('email Taken')
            else:
                user = User.objects.create_user( first_name=first_name, username=email, password=password1)
                user.save();
                print('User created')
                return redirect('login')

        else: 
            print('Password Not Matching..')  
        return redirect('/')

    else:
        return render(request,'register.html')   

def logout(request):
    auth.logout(request)
    return redirect('/') 

    
