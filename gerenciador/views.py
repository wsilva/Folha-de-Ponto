# -*- coding: utf-8 -*-

from django.http import HttpResponse

from models import RegistroPonto

def home(request):
    return HttpResponse(u"Esta é a página inicial!")

def lista(request):
    lista_registros = RegistroPonto.objects.all()
    return render_to_response("lista.html", {'lista_registros':lista_registros})