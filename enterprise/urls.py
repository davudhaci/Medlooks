
from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"   

urlpatterns = [
    path('login/',views.login,name="loginEnterprise"),
    path('register/',views.register,name="registerEnterprise"),
    path('logout/',views.logout,name="logoutEnterprise"),



]
