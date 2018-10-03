from django.contrib import admin
from django.urls import path, include
from .views import compras

urlpatterns = [
    path('', compras, name="compras"),
]
