#encoding:utf-8

from django.db import models
    

    
class Ocupacion(models.Model):
    nombre = models.CharField(max_length=50)
    def _unicode_(self):
        return self.nombre

class Categoria(models.Model):
    nombre =  models.CharField(max_length=50)
    def _unicode_(self):
        return self.nombre
      
class Usuario(models.Model):
    idUsuario = models.CharField(max_length=50)
    edad = models.TextField()
    sexo = models.CharField(max_length=1)
    ocupacion= models.ForeignKey(Ocupacion)
    codigoPostal=models.TextField()
    def _unicode_(self):
        return self.idUsuario
    
class Pelicula(models.Model):
    idPelicula = models.CharField(max_length=50)
    titulo = models.TextField()
    fechaEstreno = models.CharField(max_length=50)
    IMDbURL= models.URLField()
    categoria=models.ManyToManyField(Categoria, verbose_name=("nombre"))
    puntuacion=models.ManyToManyField(Usuario, through='Puntuacion')
    
    def _unicode_(self):
        return self.idPelicula
    
    
class Puntuacion(models.Model):
    usuario = models.ForeignKey(Usuario)
    pelicula = models.ForeignKey(Pelicula,related_name='pelicula_puntuacion')
    cantidad = models.CharField(max_length=50)