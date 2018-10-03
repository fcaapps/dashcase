from django.contrib import admin
from django.urls import path, include
from .views import cadastro_cliente

urlpatterns = [
    path('', cadastro_cliente, name="cadastro_cliente"),
]
