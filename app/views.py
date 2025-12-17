from django.shortcuts import render,redirect
from .models import *
import bcrypt
from django.http import HttpResponse
# Create your views here.

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        try:
            user = Users.objects.get(email=email)
        except:
            return HttpResponse('No user found')
        
        if not bcrypt.checkpw(password.encode('utf-8'),user.password.encode('utf-8')):
            return HttpResponse('invalid credentials')
        
        request.session['user']=user.id
        return redirect(home)

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
    if 'user' in request.session:
    # if request.session['user']:
        return render(request,'home.html')
    else:
        return redirect(login)

def logout(request):
    del request.session['user']
    return redirect(login)