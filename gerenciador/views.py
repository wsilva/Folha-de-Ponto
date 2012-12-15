# -*- coding: utf-8 -*-

from django.http import HttpResponse

def home(request):
    return HttpResponse(u"Esta é a página inicial!")