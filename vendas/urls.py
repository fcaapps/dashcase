from django.contrib import admin
from django.urls import path, include
from .views import vendas, analise_vendas

urlpatterns = [
    path('', vendas, name="vendas"),
    path('analise_vendas/', analise_vendas, name="analise_vendas"),
]
