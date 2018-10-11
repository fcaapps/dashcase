from django.contrib import admin
from django.urls import path, include
from .views import compras, acesso_negado

urlpatterns = [
    path('', compras, name="compras"),
    path('acesso_negado/', acesso_negado, name='acesso_negado')
]
