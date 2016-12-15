from principal.models import Pelicula,Usuario,Categoria
from django.shortcuts import render_to_response
import sqlite3


def inicio(request):
    return render_to_response('inicio.html')

def peliculas(request):
    peliculas = Pelicula.objects.all()
   
    return render_to_response('peliculas.html', {'peliculas':peliculas})

def categorias(request):
    categorias = Categoria.objects.all()
   
    return render_to_response('categorias.html', {'categorias':categorias})

def usuarios(request):
    cPs = []
    usuarios = Usuario.objects.all()
   
    for u in usuarios.all():
        if u.codigoPostal not in cPs:
            cPs.append(u.codigoPostal)

   
    return render_to_response('usuarios.html', {'usuarios':usuarios,'cps':cPs})

