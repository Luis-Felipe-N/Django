from dataclasses import field
from django import forms
from visitantes.models import Visitante

class VisitanteForm( forms.ModelForm ):
    class Meta:
        model = Visitante
        fields = [
            "nome_completo", "cpf", "data_nascimento",
            "numero_casa", "placa_veiculo",
        ]

        error_messages = {
            "nome_completo": {
                "required": "O nome completo é obrigatório!"
            },
            "cpf": {
                "required": "O CPF é obrigatório!"
            },
            "data_nascimento": {
                "required": "A data de nascimento é obrigatória!",
                "invalid": "Por favor, insira uma data de nascimento válida! (DD/MM/AAAA)"
            },
            "numero_casa": {
                "required": "O número da casa é obrigatório!"
            }
        }

class AutorizaVisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante