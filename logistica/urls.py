from django.contrib import admin
from django.urls import path, include
from .views import logistica, acesso_negado

urlpatterns = [
    path('', logistica, name="logistica"),
    path('acesso_negado/', acesso_negado, name='acesso_negado')
]
