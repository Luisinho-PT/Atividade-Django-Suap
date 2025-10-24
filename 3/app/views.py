from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def usuario(request, nome, idade):
    return HttpResponse(f"Olá {nome}, você tem {idade} anos!")