from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def my_logout(request):
    logout(request)
    return redirect('index')

@login_required
def teste(request):
    return render(request, 'teste.html', {'status_ativo': 'home'})
