from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Bem-vindo ao blog!")

def post(request, ano, slug):
    return HttpResponse(f"Post: {slug} ({ano})")

def autor(request, nome):
    return HttpResponse(f"Author: {nome}")
