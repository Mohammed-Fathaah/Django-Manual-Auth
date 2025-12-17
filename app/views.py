from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        print(name,email,password)
    return render(request,'register.html')

def home(request):
    return render(request,'home.html')