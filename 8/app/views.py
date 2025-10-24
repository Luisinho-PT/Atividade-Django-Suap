from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.

def arquivo(request, nome, ext):
    conteudos = {
        'pdf': 'Conteúdo do arquivo PDF.',
        'txt': 'Conteúdo do arquivo TXT.',
        'docx': 'Conteúdo do arquivo DOCX.'
    }
    
    if ext in conteudos:
        return HttpResponse(f'Arquivo: {nome}.{ext}\n{conteudos[ext]}', content_type='text/plain')
    else:
        raise Http404("Tipo de arquivo não suportado.")