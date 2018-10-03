from django.contrib import admin
from django.urls import path, include
from .views import financeiro

urlpatterns = [
    path('', financeiro, name="financeiro"),
]
