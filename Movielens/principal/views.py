from principal.models import Pelicula,Usuario,Categoria
from django.shortcuts import render_to_response
import sqlite3


def inicio(request):
    return render_to_response('inicio.html')

def peliculas(request):
    peliculas = Pelicula.objects.all()
   
    return render_to_response('peliculas.html', {'peliculas':peliculas})

