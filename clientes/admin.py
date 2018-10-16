from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Cliente
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

admin.site.site_header = 'DashCase - Painel de Administração'

class ClienteAdmin(admin.ModelAdmin):
     exclude = ('foto',)

class UserAdmin(BaseUserAdmin):
     list_filter = None


admin.site.register(Cliente, ClienteAdmin)
admin.site.unregister(Group)
