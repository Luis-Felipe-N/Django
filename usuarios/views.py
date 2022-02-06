from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    context = {
        "nome_da_pagina": "Início da dashboard"
    }

    return render(request, 'index.html', context)
    # A função render vai redenrizar um templare html assim que a função index for chamada
    # Recebe ( request, 'caminho do html', váriaveis que poderam ser usadas no template)