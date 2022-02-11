from django.contrib import admin
from django.urls import path, include

from usuarios.views import index
from visitantes.views import registrar_visitantes
from visitantes.views import informacao_visitantes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('registrar', registrar_visitantes, name="registrar_visitantes"),
    path('visitante/<id>', informacao_visitantes, name="informacao_visitante")
]
