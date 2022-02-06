from django.contrib import admin
from django.urls import path, include

from usuarios.views import index
from visitantes.views import registrar_visitantes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('visitantes', registrar_visitantes, name="registrar_visitantes")
]
