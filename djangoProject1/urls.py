"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

# app_name = 'django_web'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='my index'),
    path('inventory/',views.myinv,name='inventory'),
    path('signup/',views.Signup,name='signup'),
    path('signin/',views.Signin,name='signin'),
    path('signout/',views.Signout,name='signout'),
    path('Hire/',views.Hire,name='hire'),
    path('Buy/',views.Buy,name='buy'),
    path('training/',views.Train,name='training')
]
