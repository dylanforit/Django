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
    usuarios = []
    conn = sqlite3.connect('movielens.db')
    cursor = conn.execute("""SELECT * FROM principal_usuario group by codigoPostal""")
    
    for i in cursor:
        usuario = Usuario.objects.get(pk=i[0])
        usuarios.append(usuario)

   
    return render_to_response('usuarios.html', {'usuarios':usuarios})
