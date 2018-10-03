from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def cadastro_cliente(request):
    return render(request, 'cadastro_cliente.html', {'status_ativo': 'clientes'})
