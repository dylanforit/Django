#encoding:utf-8

from django.db import models
from pattern.db import primary_key
    
class Usuario(models.Model):
    idUsuario = models.CharField(primary_key=True,max_length=50)
    edad = models.TextField()
    localizacion = models.TextField(max_length=50)
   
    def _unicode_(self):
        return self.idUsuario
    



    
class Libro(models.Model):
    ISBN = models.CharField(primary_key=True,max_length=50)
    titulo = models.TextField()
    autor = models.TextField()
    anoPublicacion = models.CharField(max_length=50)
    editor = models.TextField()
    url_s= models.URLField()
    url_m= models.URLField()
    url_l= models.URLField()
    
    def _unicode_(self):
        return self.isbn
    
    
class Puntuacion(models.Model):
    idUsuario = models.ForeignKey(Usuario)
    isbn = models.ForeignKey(Libro)
    cantidad = models.IntegerField(range(1,10))