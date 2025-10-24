from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#tem q ter a validacao:  Valide o ano (20002030) e o mês (0112) antes de renderizar o conteúdo
def post(request, ano, mes, slug):
    if not (2000 <= int(ano) <= 2030):
        return HttpResponse("Ano inválido. O ano deve estar entre 2000 e 2030.")
    if not (1 <= int(mes) <= 12):
        return HttpResponse("Mês inválido. O mês deve estar entre 01 e 12.")
    return HttpResponse(f"Post do blog - Ano: {ano}, Mês: {mes}, Slug: {slug}")