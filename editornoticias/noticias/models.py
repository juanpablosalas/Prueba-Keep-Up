from django.db import models

import datetime

# Create your models here.

class Noticia(models.Model):
    autor = models.CharField(max_length = 50)
    titulo = models.CharField(max_length = 100)
    fecha = models.DateTimeField()
    cuerpo = models.TextField()
    
    def __str__(self):
        return self.titulo
    
    def darFecha(self):
        return self.fecha.strftime("%b %d ")
