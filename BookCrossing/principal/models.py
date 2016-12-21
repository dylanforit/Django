#encoding:utf-8
from __future__ import absolute_import
from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    idUsuario = models.CharField(primary_key=True,max_length=50)
    localizacion = models.TextField(max_length=100)
    edad = models.TextField()

    def __unicode__(self):
        return self.idUsuario

class Libro(models.Model):
    ISBN = models.CharField(max_length=50,primary_key=True)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    publicacion = models.PositiveIntegerField()
    editor = models.CharField(max_length=50)
    urlS = models.URLField()
    urlM = models.URLField()
    urlL = models.URLField()

    def __unicode__(self):
        return unicode(self.ISBN)

class Puntuacion(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro,on_delete=models.CASCADE)
    puntuacion = models.IntegerField(range(1,10))

