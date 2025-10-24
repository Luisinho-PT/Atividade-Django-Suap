from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def artigo(request, slug):
    return HttpResponse(f"Você está visualizando o artigo: {slug}")