from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
@login_required
def modelos(request):
    return render(request, 'modelos.html', {'status_ativo': 'modelos'})