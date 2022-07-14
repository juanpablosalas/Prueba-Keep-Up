from django.db import models

# Create your models here.

class Noticia(models.Model):
    autor = models.CharField(max_length = 50)
    titulo = models.CharField(max_length = 100)
    fecha = models.DateTimeField()
    noticia = models.TextField()
    
    def __str__(self):
        return self.titulo
