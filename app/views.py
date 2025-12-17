from django.shortcuts import render,redirect
from .models import *
import bcrypt
from django.http import HttpResponse
# Create your views here.

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        
        if Users.objects.filter(email=email).exists():
            return HttpResponse('User already exists')
        
        hashed_password=bcrypt.hashpw(
            password.encode('utf-8'),bcrypt.gensalt()
        )

        data=Users.objects.create(name=name,email=email,password=hashed_password.decode('utf-8'))
        data.save()
        return redirect(login)
    return render(request,'register.html')

def home(request):
    return render(request,'home.html')