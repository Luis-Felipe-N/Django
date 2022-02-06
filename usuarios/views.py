from django.shortcuts import render
from visitantes.models import Visitante

def index(request):

    todos_visitantes = Visitante.objects.all()
    # Buscando todos visitantes e armazenando na váriavel

    context = {
        "nome_da_pagina": "Início da dashboard",
        "todos_visitantes": todos_visitantes
    }

    return render(request, 'index.html', context)
    # A função render vai redenrizar um templare html assim que a função index for chamada
    # Recebe ( request, 'caminho do html', váriaveis que poderam ser usadas no template)