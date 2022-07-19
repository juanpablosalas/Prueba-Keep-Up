from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib import messages

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

    return render(request,'home.html',{'object_list':noticias, 'justadded': False, 'justdeleted': False})

def detail(request, pk):
    print("-- La recibe")
    noti = Noticia.objects.get(id=pk)
    delete_warning= False
    modified_warning = False
    
    if request.method == 'POST':
        if request.POST.get("delete"):
            delete_warning = True
        elif request.POST.get("confirm-delete"):
            delete_warning = True
            Noticia.objects.filter(id=pk).delete()
            return render(request,'home.html',{'object_list':Noticia.objects.all(), 'justadded': False, 'justdeleted': True})  
        elif request.POST.get("cancel-delete"):
            delete_warning = False
                

    return render(request, 'detail.html', {'noticia': noti, 'warning': delete_warning, 'modified': modified_warning})


def add(request):
    
    error_warning = False
    
    if request.method == 'POST':
        
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        fecha = datetime.now()
        cuerpo = request.POST['cuerpo']
        
        
        
        if(titulo=="" or autor =="" or cuerpo==""):
                error_warning = True
        else:
            
            Noticia.objects.create(
                autor = autor, 
                titulo = titulo, 
                fecha=fecha, cuerpo=cuerpo)
            return render(request,'home.html',{'object_list':Noticia.objects.all(), 'justadded': True, 'justdeleted': False})
        
        
        
        
    return render(request, 'add.html', {'warning': error_warning})

def edit(request, pk):
    noti = Noticia.objects.get(id=pk)
    
    if request.method == 'POST':
        
        if request.POST.get("modify"):
            
            titulo = request.POST['titulo']
            autor = request.POST['autor']
            cuerpo = request.POST['cuerpo']
            
            noti.titulo = titulo
            noti.autor = autor
            noti.cuerpo = cuerpo
            noti.save()

            delete_warning = False
            modified_warning = True
            
            return render(request, 'detail.html', {'noticia': noti, 'warning': delete_warning, 'modified': modified_warning})
        
    
    return render(request, 'edit.html', {'noticia': noti})
    
    
        
        
