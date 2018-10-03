from django.contrib import admin
from django.urls import path, include
from .views import index, my_logout, teste

urlpatterns = [
    path('', index, name="index"),
    path('teste/', teste, name="teste"),
    path('logout/', my_logout, name="my_logout")
]
