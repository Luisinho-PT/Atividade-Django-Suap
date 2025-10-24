from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def boas_vindas(request):
    return HttpResponse("Bem-vindo ao meu site Django!")