from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mostra_numero(request, num):
    return HttpResponse(f"O número fornecido é: {num}")