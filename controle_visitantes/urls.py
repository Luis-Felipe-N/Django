from django.contrib import admin
from django.urls import path, include

from usuarios.views import index
from visitantes.views import registrar_visitantes, informacao_visitantes, finalizar_visita

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('registrar', registrar_visitantes, name="registrar_visitantes"),
    path('visitante/<int:id>', informacao_visitantes, name="informacao_visitante"),
    path('visitante/<int:id>/finalizar-visita', finalizar_visita, name="finalizar_visita")
]
