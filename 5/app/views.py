from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def perfil(request, nome=None):
    if nome:
        return HttpResponse(f"Perfil do usuário: {nome}")
    else:
        return HttpResponse("Perfil de Visitante")