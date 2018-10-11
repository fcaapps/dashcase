from django.contrib import admin
from django.urls import path, include
from .views import vendas, analise_vendas, analise_vendas_d, acesso_negado

urlpatterns = [
    path('', vendas, name="vendas"),
    path('analise_vendas/relatorio/', analise_vendas, name="analise_vendas"),
    path('analise_vendas/dashboard/', analise_vendas_d, name="analise_vendas_d"),
    path('acesso_negado/', acesso_negado, name='acesso_negado')
]
