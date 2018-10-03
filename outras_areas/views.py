from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
@login_required
def outras_areas(request):
    return render(request, 'outras_areas.html', {'status_ativo': 'outras_areas'})