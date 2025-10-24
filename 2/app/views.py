from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def produto(request, nome):
    return HttpResponse(f'Produto: {nome.replace("-", " ").title()}')