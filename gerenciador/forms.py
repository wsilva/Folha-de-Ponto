# -*- coding: utf-8 -*-

from django import forms

class FormRegistroPonto(forms.Form):
    dia = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=['%d/%m/%Y', '%d/%m/%y']
        )
    hora = forms.TimeField()
    tipo = forms.CharField()
    imagem = forms.ImageField()