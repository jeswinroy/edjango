from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def  home_view(request):
    return render(request, 'pages/index.html')

def  register_view(request):

    if request.method == 'POST':
        
        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(email,email=email,password=password)
        user.save()
        login(request,user)
        return redirect('/dashboard')

    return render(request, 'pages/register.html')

