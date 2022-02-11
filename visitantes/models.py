from django.db import models

# Create your models here.

class Visitante(models.Model):
    nome_completo = models.CharField(
        verbose_name="Nome completo", max_length=194
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11,
    )

    data_nascimento = models.DateField(
        verbose_name="Data de nascimento",
        auto_now=False
    )

    numero_casa = models.CharField(
        verbose_name="Número da casa a ser visitada",
        max_length=3,
    )

    horario_chegada = models.DateTimeField(
        verbose_name="Horário de chegada na recepção", auto_now_add=True
    )

    horario_autorizacao = models.DateTimeField(
        verbose_name="Horário de autorização de entrada",
        null=True,
        blank=True,
        auto_now=False,
    )

    horario_saida = models.DateTimeField(
        verbose_name="Horário de saída do condomínio",
        null=True,
        blank=True,
        auto_now=False,
    )

    registrado_por = models.ForeignKey(
        "porteiros.Porteiro",
        verbose_name="Porteiro responsável pelo registro",
        on_delete=models.CASCADE,
    )

    placa_veiculo = models.CharField(
        verbose_name="Placa do veículo",
        max_length=10,
        blank=True,
        null=True,
    )

    morador_responsavel = models.CharField(
        verbose_name="Nome do morador responsável por autorizar a entrada do visitante",
        max_length=194,
        blank=True,
        null=True,
    )
    class Meta:
        verbose_name = 'Visitante'
        verbose_name_plural = 'Visitantes'
        db_table = 'visitante'
    
    def __str__(self):
        return self.nome_completo