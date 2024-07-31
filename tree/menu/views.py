from django.shortcuts import render
from .models import Menu

def home(request):
    return render(request, 'base.html')