# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from thumbs import ImageWithThumbsField

class RegistroPonto(models.Model):

    # datahora = models.DateTimeField()
    dia = models.DateField()
    hora = models.TimeField()

    TIPOS = (
        ('ent', 'Entrada'),
        ('sa', 'Saída para almoço'),
        ('va', 'Volta do almoço'),
        ('sai', 'Saída'),
    )
    tipo = models.CharField(max_length=3, choices=TIPOS)

    imagem = ImageWithThumbsField(upload_to='comprovantes', sizes=((200,150),))

    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return u"%s - %s %s" % (self.dia, self.hora, self.tipo)

    # para mudar o nome da tabela
    # class Meta:
        # db_table = "tbl_registro_ponto"

