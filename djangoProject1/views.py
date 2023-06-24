from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.hashers import make_password

def Home(request):
    return render(request,'index.html')
def myinv(request):
    return render(request,'inventory.html')
def Signup(request):
    if request.method =="POST":
        username = request.POST.get("username")
        print("Username:", username)
        Fname= request.POST.get("Fname")
        Lname= request.POST.get("Lname")
        Email= request.POST.get("email")
        password1=request.POST.get("password1")
        password2= request.POST.get("password2")
        if password1 == password2:
            hashed_password = make_password(password1)
            myuser = User.objects.create_user(username=username, email=Email, password=hashed_password)
            myuser.first_name = Fname
            myuser.last_name = Lname
            myuser.save()
            messages.success(request, "Account successfully created")
            return redirect('/signin')
        else:
            # Handle password mismatch error
            return render(request, 'signup.html', {'error': 'Passwords do not match.'})

    return render(request,'signup.html')

def Signin(request):
    if request.method =="POST":
        username= request.POST.get("username")
        password= request.POST.get("password")
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            Fname=user.first_name
            return render(request,"index.html",{Fname:Fname})
        else:
            error = "Invalid username or password."
            return render(request, 'signin.html',{'error':error})
            # return redirect('/')
    return render(request,'signin.html')
def Signout(request):
    logout (request)
    messages.success("logged out successfully")
    return redirect('/')
def Hire(request):
    if request.method=="Post":
        name=request.POST.get("name")
        email=request.POST.get("email")
        equipment=request.POST.get("equipment")
        number=request.POST.get("phone")
        days= request.POST.get("days")
        quantity=request.POST.get("quantity")

    return render(request,'Hire.html')
def Buy(request):
    return render(request,'Buy.html')
def Train(request):
    return render(request,'training.html')