# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.http import Http404

from models import RegistroPonto

from forms import FormRegistroPonto

# @login_required
def home(request):
    return HttpResponse(u"Esta é a página inicial!")

# @login_required
def lista(request):
    lista_registros = RegistroPonto.objects.all()
    return render_to_response("lista.html", {'lista_registros':lista_registros}, context_instance=RequestContext(request))

# @login_required
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

# @login_required
def editar(request, id_registro):
    # try:
    #     registro = RegistroPonto.objects.get(pk=id_registro)
    # except RegistroPonto.DoesNotExist:
    #     raise Http404()

    # return render_to_response()
    registro = get_object_or_404(RegistroPonto, pk=id_registro)
    if request.method == "POST":
        form = FormRegistroPonto(request.POST, request.FILES, instance=registro)
        if form.is_valid():
            form.save()
            return render_to_response("gravado.html",{})
    else:
        form=FormRegistroPonto(instance=registro)

    return render_to_response("editar.html",{'form':form}, context_instance=RequestContext(request))

def remover(request, id_registro):
    registro = get_object_or_404(RegistroPonto, pk=id_registro)
    if request.method == 'POST':
        registro.delete()
        return render_to_response("removido.html", {})
    return render_to_response("remove.html", {"registro":registro}, context_instance = RequestContext(request))


