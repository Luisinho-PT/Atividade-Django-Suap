from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def soma(request, a, b):
    resultado = a + b
    return HttpResponse(f"A soma de {a} e {b} é {resultado}")