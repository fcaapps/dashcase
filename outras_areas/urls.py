from django.contrib import admin
from django.urls import path, include
from .views import outras_areas

urlpatterns = [
    path('', outras_areas, name="outras_areas"),
]
