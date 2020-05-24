from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def  home_view(request):
    return render(request, 'dashboard/index.html')

@login_required(login_url='/login')
def  profile_view(request):
    return render(request, 'dashboard/profile.html')

