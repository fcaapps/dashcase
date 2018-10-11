from django.contrib import admin
from django.urls import path, include
from .views import cadastro_cliente, acesso_negado

urlpatterns = [
    path('', cadastro_cliente, name="cadastro_cliente"),
    path('acesso_negado/', acesso_negado, name='acesso_negado')
]
