from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Noticia

from datetime import datetime

#class VistaNoticias(ListView):
#    model = Noticia
#    template_name = 'home.html'
    
class VistaNoticiaDetallada(DetailView):
    model = Noticia
    template_name = 'detail.html'

# Create your views here.

def home(request):
    noticias = Noticia.objects.all()

    return render(request,'home.html',{'object_list':noticias})

def detail(request, pk):
    noti = Noticia.objects.get(id=pk)
    return render(request, 'detail.html', {'noticia': noti})


def add(request):
    
    if request.method == 'POST':
        
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        fecha = datetime.now()
        cuerpo = request.POST['cuerpo']
        
        noticia = Noticia.objects.create(
            autor = autor, 
            titulo = titulo, 
            fecha=fecha, 
            cuerpo=cuerpo)
        
        return render(request,'home.html',{'object_list':Noticia.objects.all()})
        
    return render(request, 'add.html')
        
        
