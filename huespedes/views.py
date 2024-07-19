from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from huespedes.models import Huesped
from huespedes.forms import BuscarHuesped
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class Huespedes(ListView):
    model=Huesped
    template_name='huespedes/huespedes.html'
    context_object_name='huespedes'
    
    def get_queryset(self):
        nombre=self.request.GET.get('nombre', '')
        huespedes=self.model.objects.filter(nombre__icontains=nombre)
        return huespedes
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["formulario"]=BuscarHuesped()
        context['nombre']=self.request.GET.get('nombre','')
        return context
    
class CrearHuesped(LoginRequiredMixin,CreateView):
    model=Huesped
    template_name='huespedes/crear_huesped.html'
    success_url=reverse_lazy('huespedes')
    fields=['nombre','apellido','nacionalidad','fecha_de_nacimiento']
    
class EliminarHuesped(LoginRequiredMixin,DeleteView):
    model=Huesped
    template_name='huespedes/eliminar_huesped.html'
    success_url=reverse_lazy('huespedes')
    
class ActualizarHuesped(LoginRequiredMixin,UpdateView):
    model=Huesped
    template_name='huespedes/actualizar_huesped.html'
    success_url=reverse_lazy('huespedes')
    fields=['nombre','apellido','nacionalidad','fecha_de_nacimiento']
    
class VerHuesped(DetailView):
    model=Huesped
    template_name='huespedes/ver_huesped.html'
    
    
    
    



