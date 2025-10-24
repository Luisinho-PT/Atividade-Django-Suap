from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def saudacao(request, nome):
    return HttpResponse(f"Olá, {nome}! Seja bem-vindo ao nosso site.")
