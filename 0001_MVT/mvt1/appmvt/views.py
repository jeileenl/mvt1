from django.shortcuts import render
from django.http import HttpResponse
from appmvt.models import Familiares

def lista_familiares(request):
    familia = Familiares.objects.all ()
    return HttpResponse (familia[3].edad)
    