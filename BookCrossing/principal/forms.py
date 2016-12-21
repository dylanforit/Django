#encoding:utf-8
from django.forms import ModelForm
from django import forms
from principal.models import Libro, Usuario, Puntuacion

class LibrosPuntutadosUsuarioForm(forms.Form):
    idUsuario = forms.IntegerField(label='Id de usuario')