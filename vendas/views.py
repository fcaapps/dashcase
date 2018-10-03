from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
@login_required
def vendas(request):
    return render(request, 'vendas.html', {'status_ativo': 'modelos'})