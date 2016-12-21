from django.db import models

class Artista(models.Model):
    idArtista = models.CharField(primary_key=True,max_length=50)
    nombre = models.TextField(max_length=100)
    url = models.URLField()
    pictureURL = models.URLField()
    
    def __unicode__(self):
        return unicode(self.idArtista)

class Etiqueta(models.Model):
    idTag = models.CharField(primary_key=True,max_length=50)
    tagValue = models.TextField(max_length=100)
    
    def __unicode__(self):
        return unicode(self.idTag)
    
class UsuarioArtista(models.Model):
    idUsuario = models.CharField(max_length=50)
    artista = models.ForeignKey(Artista)
    tiempoEscucha = models.PositiveIntegerField()
    
    def __unicode__(self):
        return unicode(self.tiempoEscucha)

class UsuarioEtiquetaArtista(models.Model):
    idUsuario = models.CharField(max_length=50)
    artista = models.ForeignKey(Artista)
    tag = models.ForeignKey(Etiqueta)
    dia = models.PositiveIntegerField()
    mes = models.PositiveIntegerField()
    ano = models.PositiveIntegerField()
    
    def __unicode__(self):
        return unicode(self.ano)
    
class UsuarioAmigo(models.Model):
    idUsuario = models.CharField(max_length=50)
    idAmigo = models.CharField(max_length=50)
    
    def __unicode__(self):
        return unicode(self.idAmigo)