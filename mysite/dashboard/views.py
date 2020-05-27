from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import logout,login

@login_required(login_url='/login')
def  home_view(request):
    return render(request, 'dashboard/index.html')

@login_required(login_url='/login')
def  profile_view(request):
    user = User.objects.get(username=username)
    return render(request, 'dashboard/profile.html', {"user":user}) 


@login_required(login_url='/login')
def  logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login')
def change_password(request):
    context={}
    if request.method=="POST":
        current = request.POST["cpwd"]
        new_pas = request.POST["npwd"]
        
        user = User.objects.get(id=request.user.id)
        un = user.username
        check = user.check_password(current)
        if check==True:
            user.set_password(new_pas)
            user.save()
            context["msz"] = "Password Changed Successfully!!!"
            context["col"] = "alert-success"
            user = User.objects.get(username=un)
            login(request,user)
        else:
            context["msz"] = "Incorrect Current Password"
            context["col"] = "alert-danger"

    return render(request,"dashboard/change_password.html",context)





