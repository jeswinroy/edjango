from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('profile', views.profile_view, name='profile'),
    path('change_password', views.profile_view, name='change_password'),
    path('logout', views.logout_view, name='logout'),    
]
