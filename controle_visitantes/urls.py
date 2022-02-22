from re import template
from unicodedata import name
from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

from dashboard.views import index
from visitantes.views import registrar_visitantes, informacao_visitantes, finalizar_visita

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('registrar', registrar_visitantes, name="registrar_visitantes"),
    path('visitante/<int:id>', informacao_visitantes, name="informacao_visitante"),
    path('visitante/<int:id>/finalizar-visita', finalizar_visita, name="finalizar_visita"),
    path('login/', auth_views.LoginView.as_view(
        template_name="login.html"
    ), name="login"),
    path(
        'logout/', auth_views.LogoutView.as_view(
        template_name="logout.html"
    ), name="logout")
]
