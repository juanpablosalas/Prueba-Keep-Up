from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Noticia

class VistaNoticias(ListView):
    model = Noticia
    template_name = 'home.html'
    
class VistaNoticiaDetallada(DetailView):
    model = Noticia
    template_name = 'detail.html'

# Create your views here.
