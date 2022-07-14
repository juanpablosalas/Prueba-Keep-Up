from django.shortcuts import render
from django.views.generic import ListView
from . models import Noticia

class VistaNoticias(ListView):
    model = Noticia
    template_name = 'home.html'

# Create your views here.
