# -*- coding: utf-8 -*-

from django.contrib import admin

from models import RegistroPonto

# admin.site.register(RegistroPonto)

class RegistroPontoAdmin(admin.ModelAdmin):
    fields = ('dia', 'hora', 'tipo', 'imagem')
    list_display = ('dia', 'hora', 'tipo')

admin.site.register(RegistroPonto, RegistroPontoAdmin)