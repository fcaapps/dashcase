from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, reverse

@login_required
def logistica(request):
    user = request.user
    if user.has_perm('clientes.logistica_permissoes'):
        return render(request, 'logistica.html', {'status_ativo': 'logistica'})
    else:
        return redirect(reverse('acesso_negado'))

@login_required
def acesso_negado(request):
    return render(request, 'acesso_negado.html')
