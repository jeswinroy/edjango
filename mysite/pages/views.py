from django.shortcuts import render,redirect
from django.http import HttpResponse

def  home_view(request):
    return render(request, 'pages/index.html')

def  register_view(request):

    if request.method == 'POST':
        full_name = request.POST['full_name']
        return HttpResponse(full_name)

    return render(request, 'pages/register.html')

