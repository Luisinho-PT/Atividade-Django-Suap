from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def download(request, nome, ext):
    return HttpResponse(f"Você solicitou o download do arquivo: {nome}.{ext}")