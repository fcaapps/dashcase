from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
@login_required
def logistica(request):
    return render(request, 'logistica.html', {'status_ativo': 'logistica'})