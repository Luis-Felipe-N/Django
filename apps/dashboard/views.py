from django.shortcuts import render
from visitantes.models import Visitante
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def index(request):

    todos_visitantes = Visitante.objects.all().order_by('-horario_chegada')
    # Buscando todos visitantes e armazenando na váriavel

    visitantes_aguardando = todos_visitantes.filter( status="AGUARDANDO")
    visitantes_em_visita = todos_visitantes.filter( status="EM_VISITA")
    visitantes_finalizado = todos_visitantes.filter( status="FINALIZADO")
    visitante_mes = todos_visitantes.filter( horario_chegada__month=timezone.now().month )

    context = {
        "nome_da_pagina": "Início da dashboard",
        "todos_visitantes": todos_visitantes,
        "visitantes_aguardando": visitantes_aguardando.count(),
        "visitantes_em_visita": visitantes_em_visita.count(),
        "visitantes_finalizado": visitantes_finalizado.count(),
        "visitante_mes": visitante_mes.count()
    }

    return render(request, 'index.html', context)
    # A função render vai redenrizar um templare html assim que a função index for chamada
    # Recebe ( request, 'caminho do html', váriaveis que poderam ser usadas no template)