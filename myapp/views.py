from django.shortcuts import render
from django.http import HttpResponse

def add(request):
    return render(request, 'index.html')
