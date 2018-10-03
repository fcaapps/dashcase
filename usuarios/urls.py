from django.contrib import admin
from django.urls import path, include
from .views import cadastro_usuario

urlpatterns = [
    path('', cadastro_usuario, name="cadastro_usuario"),
]
