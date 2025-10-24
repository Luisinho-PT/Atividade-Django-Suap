from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def data(request, ano, mes):
    return HttpResponse(f"Ano: {ano}, Mês: {mes}")
