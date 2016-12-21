#enconding:utf-8
from principal.models import Libro,Puntuacion,Usuario
from django.shortcuts import render_to_response
from principal.forms import LibrosPuntutadosUsuarioForm
from django.template import RequestContext
import sqlite3


def inicio(request):
    return render_to_response('inicio.html')

# def peliculas(request):
#     peliculas = Libro.objects.all()
#    
#     return render_to_response('peliculas.html', {'peliculas':peliculas})

def categorias(request):
    categorias = Libro.objects.all()
   
    return render_to_response('categorias.html', {'categorias':categorias})

def buscaPuntuacionesUsuarios(request):
    resultado = []
    conn = sqlite3.connect('bookCrossing.db')
    
    if request.method == 'POST':
        formulario = LibrosPuntutadosUsuarioForm(request.POST)
        if formulario.is_valid():
            formulario = LibrosPuntutadosUsuarioForm(request.POST)
            if formulario.is_valid():
                id = formulario.cleaned_data['idUsuario']
                puntuaciones = Puntuacion.objects.filter(usuario=id)#aqui falla
                for p in puntuaciones:
                    peli = conn.execute("""SELECT (titulo, ISBN) from principal_libro where ISBN = ?;""", (p.libro))
                    resultado.append(peli[0]+" - "+peli[1]+":  "+str(p.cantidad))
                return render_to_response('librosPorPuntuacion.html', {'resultado': resultado})
    else:
        formulario = LibrosPuntutadosUsuarioForm()
        return render_to_response('formPuntuacionesUsuario.html', {'formulario': formulario}, context_instance=RequestContext(request))

