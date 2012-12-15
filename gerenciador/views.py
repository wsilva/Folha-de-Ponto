# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import RegistroPonto

from forms import FormRegistroPonto

def home(request):
    return HttpResponse(u"Esta é a página inicial!")

def lista(request):
    lista_registros = RegistroPonto.objects.all()
    return render_to_response("lista.html", {'lista_registros':lista_registros})

def novo(request):
    if request.method == 'POST':
        form = FormRegistroPonto(request.POST, request.FILES)
        if form.is_valid():
            dados = form.cleaned_data
            registroponto = RegistroPonto(
                dia = dados['dia'],
                hora = dados['hora'],
                tipo = dados['tipo'],
                imagem = ''
                )
            registroponto.save()

            return render_to_response("gravado.html",{})

    else:
        form = FormRegistroPonto()

    return render_to_response("novoregistro.html",{'form':form}, context_instance=RequestContext(request))