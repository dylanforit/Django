#encoding:utf-8
from django.forms import ModelForm
from django import forms
from principal.models import Pelicula, Usuario, Puntuacion, Categoria, Ocupacion

class PeliculasAnoForm(forms.Form):
    ano = forms.IntegerField(label='Ano de estreno')

class PeliculasPuntutadasUsuarioForm(forms.Form):
    idUsuario = forms.IntegerField(label='Id de usuario')