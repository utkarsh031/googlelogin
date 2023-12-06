from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import logout
from home.models import Regi
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect('/login')

    return render(request,"index.html")
def logout_view(request):
    logout(request)
    return redirect('/') 
def regi(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password =request.POST.get('password')
        phone=request.POST.get('phone')
        if name:
            regi = Regi(name=name, email=email, phone=phone)
            regi.save()
            messages.success(request, "Profile details updated.")
        else:
   
            return HttpResponse("Error: Name cannot be empty.")
        
    return render(request,'regi.html')
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)

        if user is not None:
            # A backend authenticated the credentials
            return redirect('/')
        else:
            # No backend authenticated the credentials
            return render(request, "login.html")

    return render(request, "login.html")
  