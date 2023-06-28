from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse

def Home(request):
    current_user = request.user
    print(current_user)
    return render(request,'index.html',{'user':current_user})
def myinv(request):
    return render(request, 'inventory.html')
def Signup(request):
    if request.method =="POST":
        username = request.POST.get("username")
        Fname= request.POST.get("Fname")
        Lname= request.POST.get("Lname")
        Email= request.POST.get("email")
        password1=request.POST.get("password1")
        password2= request.POST.get("password2")
        if password1 == password2:
            myuser = User.objects.create_user(username=username, email=Email, password=password1)
            myuser.first_name = Fname
            myuser.last_name = Lname
            myuser.save()
            user = authenticate(request, username=username, password=password1)
            if user is not None:
                login(request, user)
                return render(request, "index.html")
            else:
                return render(request, 'signup.html')
            # messages.success(request, "Account successfully created")
            # return redirect('/signin')
        else:
            # Handle password mismatch error
            return render(request, 'signup.html', {'error': 'Passwords do not match.'})

    return render(request,'signup.html')

def Signin(request):
    if request.method =="POST":
        username= request.POST.get("username")
        password= request.POST.get("password")
        user=authenticate(request, username=username, password=password)
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
    # messages.success("logged out successfully")
    return redirect('/')
def Hire(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        equipment=request.POST.get("equipment")
        number=request.POST.get("phone")
        days= request.POST.get("days")
        quantity=request.POST.get("quantity")
        return render(request, 'Hire.html', {"message":"Equipment Hired"})
    else:
        current_user = request.user
        equipment = request.GET.get("equipment")
        price = request.GET.get("price")
        data = {
                "user":current_user,
                "equipment":equipment,
                "price":price
                }
    return render(request,'Hire.html',{"data":data})
def Buy(request):
    return render(request,'Buy.html')
def Train(request):
    return render(request,'training.html')