from django.db import models

# Create your models here.

class Visitante():

    

    class Meta():
        verbose_name = 'Visitante'
        verbose_name_plural = 'Visitantes'
        db_table = 'visitante'