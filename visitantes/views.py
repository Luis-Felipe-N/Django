from django.shortcuts import render
from visitantes.forms import VisitanteForm

def registrar_visitantes( request ):

    form = VisitanteForm

    context = {
        "nome_pagina": "Registrar visitantes",
        "form": form
    }

    return render( request , 'registrar_visitante.html', context )