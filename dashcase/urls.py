"""dashcase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken import views
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

from api.views import DadosPerfilViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'perfis', DadosPerfilViewSet)
urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('clientes/', include('clientes.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('modelos/', include('modelos.urls')),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls+[path('auth', views.obtain_auth_token)])),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
