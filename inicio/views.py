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



