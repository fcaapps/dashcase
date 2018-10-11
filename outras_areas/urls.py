from django.contrib import admin
from django.urls import path, include
from .views import outras_areas, acesso_negado

urlpatterns = [
    path('', outras_areas, name="outras_areas"),
    path('acesso_negado/', acesso_negado, name='acesso_negado'),
]
