# -*- coding: utf-8 -*-

from django.contrib import admin

from models import RegistroPonto

# admin.site.register(RegistroPonto)

class RegistroPontoAdmin(admin.ModelAdmin):
    fields = ('dia', 'hora', 'tipo', 'imagem')
    list_display = ('dia', 'hora', 'tipo')

    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()

    def queryset(self,request):
        qs = super(RegistroPontoAdmin, self).queryset(request)
        return qs.filter(usuario = request.user)



admin.site.register(RegistroPonto, RegistroPontoAdmin)