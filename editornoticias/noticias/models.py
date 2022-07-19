from django.db import models

import datetime

import locale

# Idioma "es-ES" (código para el español de España)
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8') 

# Create your models here.

class Noticia(models.Model):
    autor = models.CharField(max_length = 50)
    titulo = models.CharField(max_length = 100)
    fecha = models.DateTimeField()
    cuerpo = models.TextField()
    
    def __str__(self):
        return self.titulo
    
    def darFecha(self):
        return self.fecha.strftime("%b ").capitalize()+self.fecha.strftime("%d")
    
    def darFechaDetalle(self):
        return self.fecha.strftime("%d de %B ")
