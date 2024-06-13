from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.template import Template,Context,loader
from datetime import datetime
import random
from inicio.models import Huesped
from inicio.forms import HuespedFormulario

# Create your views here.
def inicio(request):
    return render(request, 'inicio/inicio.html')

def crear_huesped(request):
    formulario=HuespedFormulario()
    if request.method=='POST':
        formulario=HuespedFormulario(request.POST)
        if formulario.is_valid():
            datos=formulario.cleaned_data
            huesped=Huesped(nombre=datos.get('nombre'),apellido=datos.get('apellido'),edad=datos.get('edad'),nacionalidad=datos.get('nacionalidad'))
            huesped.save()
            return redirect('inicio')                                  
    return render(request,'inicio\crear_huesped.html',{'formulario':formulario})

def huespedes(request):
    huespedes=Huesped.objects.all()
    return render(request,'inicio/huespedes.html',{'huespedes':huespedes})