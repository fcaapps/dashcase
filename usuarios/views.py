from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def cadastro_usuario(request):
    return render(request, 'cadastro_usuario.html', {'status_ativo': 'usuarios'})