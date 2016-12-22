#encoding:utf-8
from django.forms import ModelForm
from django import forms


class ArtistasPorUsuarioForm(forms.Form):
    id = forms.IntegerField(label='Id de usuario')