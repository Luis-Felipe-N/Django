from django.contrib import messages
from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404

from visitantes.models import Visitante
from visitantes.forms import VisitanteForm


def registrar_visitantes(request):

    form = VisitanteForm()

    if request.method == 'POST':
        form = VisitanteForm(request.POST)

        if form.is_valid():
            visitante = form.save(commit=False)
            visitante.registrado_por = request.user.porteiro

            visitante.save()

            messages.success(
                request,
                "Visitante registrado com sucesso"
            )

            return redirect("index")

    context = {
        'nome_pagina': 'Registrar visitantes',
        'form': form
    }

    return render( request, 'registrar_visitante.html', context)

def informacao_visitantes(request, id):

    visitante = get_object_or_404(Visitante, id=id)

    print('Esse é o vsitante encontrado: ')
    print(id, visitante)

    context = {
        "nome_pagina": "Informação do visitante",
        "visitante": visitante
    }

    return render(request, 'informacoes_visitante.html', context)