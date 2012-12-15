# -*- coding: utf-8 -*-

from django.db import models

class RegistroPonto(models.Model):

    # datahora = models.DateTimeField()
    dia = models.DateField()
    hora = models.TimeField()
    tipo = models.CharField(max_length=100)
    imagem = models.CharField(max_length=100)

    # para mudar o nome da tabela
    # class Meta:
        # db_table = "tbl_registro_ponto"

