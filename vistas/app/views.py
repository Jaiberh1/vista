from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import libros
from django import forms
from django.urls import reverse
from django.contrib import messages



class CrearLibro(SuccessMessageMixin,CreateView):
    model = libros
    form = libros
    fields = "__all__"
    success_message = 'Libro Creado Correctamente !'
 
class ListarLibros(ListView):
    model = libros
 
class DetalleLibro(DetailView):
    model = libros
 
class ActualizarLibros(SuccessMessageMixin, UpdateView):
    model = libros
    form = libros
    field = "__all__"
    def get_success_url(self):
        return reverse('leer')
   
class EliminarLibro (SuccessMessageMixin, DeleteView):
    model = libros
    form = libros
    field = "__all__"
    def get_success_url(self):
        success_message = 'Libro Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leer')