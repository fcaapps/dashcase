from django.contrib import admin
from django.urls import path, include
from .views import financeiro, acesso_negado

urlpatterns = [
    path('', financeiro, name="financeiro"),
    path('acesso_negado/', acesso_negado, name='acesso_negado')
]
