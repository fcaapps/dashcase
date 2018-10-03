from django.contrib import admin
from django.urls import path, include
from .views import modelos

urlpatterns = [
    path('', modelos, name="modelos"),
    path('vendas/', include('vendas.urls')),
    path('compras/', include('compras.urls')),
    path('financeiros/', include('financeiro.urls')),
    path('logistica/', include('logistica.urls')),
    path('outras_areas/', include('outras_areas.urls'))

]
