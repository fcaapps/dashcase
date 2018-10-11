from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, reverse

@login_required
def cadastro_cliente(request):
    user = request.user
    if user.has_perm('clientes.clientes_permissoes'):
        return render(request, 'cadastro_cliente.html', {'status_ativo': 'clientes'})
    else:
        return redirect(reverse('acesso_negado'))

@login_required
def acesso_negado(request):
    return render(request, 'acesso_negado.html')
