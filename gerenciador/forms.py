# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm

from gerenciador.models import RegistroPonto

# class FormRegistroPonto(forms.Form):
#     dia = forms.DateField(
#         widget=forms.DateInput(format='%d/%m/%Y'),
#         input_formats=['%d/%m/%Y', '%d/%m/%y']
#         )
#     hora = forms.TimeField()
#     tipo = forms.CharField()
#     imagem = forms.ImageField()

class FormRegistroPonto(forms.ModelForm):
    dia = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=['%d/%m/%Y', '%d/%m/%y']
        )
    imagem = forms.ImageField()
    class Meta:
        model = RegistroPonto
        fields = ('dia', 'hora', 'tipo', 'imagem')