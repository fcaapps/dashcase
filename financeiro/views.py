from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
@login_required
def financeiro(request):
    return render(request, 'financeiro.html', {'status_ativo': 'financeiro'})