from django.contrib import admin
from django.urls import path, include
from .views import modelos, acesso_negado

urlpatterns = [
    path('', modelos, name="modelos"),
    path('vendas/', include('vendas.urls')),
    path('compras/', include('compras.urls')),
    path('financeiros/', include('financeiro.urls')),
    path('logistica/', include('logistica.urls')),
    path('outras_areas/', include('outras_areas.urls')),
    path('acesso_negado/', acesso_negado, name='acesso_negado'),

]
