import datetime
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#valide usando  datetime.strptime
def agenda(request, data):
    if datetime.datetime.strptime(data, '%d-%m-%Y'):
        return HttpResponse(f"Data informada: {data}")
    else:
        return HttpResponse("Data inválida")