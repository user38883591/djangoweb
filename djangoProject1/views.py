from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse

def Home(request):
    return render(request,'index.html')
def myinv(request):
    return render(request,'inventory.html')
def Signup(request):
    if request.method =="post":
        username = request.POST.get("Username")
        Fname= request.POST.get("Fname")
        Lname= request.POST.get("Lname")
        Email= request.POST.get("Email")
        password1=request.POST.get("password1")
        password2= request.POST.get("password2")

        myuser= User.objects.create_user(username,Email,password1)
        myuser.first_name=Fname
        myuser.last_name=Lname

        myuser.save()
        messages.success(request,"Account successfully created")
        return redirect(reverse ('success'))

    return render(request,'signup.html')
def Signin(request):
    if request.method =="POST":
        username= request.POST.get("username")
        password1= request.POST.get("password1")
        user=authenticate(username=username,password1=password1)
        if user is None:
            login(request,user)
            Fname=user.first_name
            return render(request,"index.html",{Fname:Fname})
        else:
            messages.error(request,"Wrong credentials")
            return redirect('/')
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