from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def email(request, email):
    return HttpResponse(f"O email fornecido é: {email}")