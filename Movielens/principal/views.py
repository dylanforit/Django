from principal.models import Pelicula,Usuario,Categoria
from django.shortcuts import render_to_response
from principal.forms import PeliculasAnoForm, PeliculasPuntutadasUsuarioForm
from django.template import RequestContext
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
        if u.ocupacion not in cPs:
            cPs.append(u.ocupacion)

   
    return render_to_response('usuarios.html', {'usuarios':usuarios,'cps':cPs})

def peliculasPuntuadas(request):
    peliculasPuntuadas = []
    conn = sqlite3.connect('movielens.db')
    cursor = conn.execute("""SELECT pelicula_id, avg(cantidad) as c FROM principal_puntuacion group by pelicula_id order by c DESC LIMIT 5""")
    for i in cursor:
        pelicula = Pelicula.objects.get(pk=i[0])
        peliculasPuntuadas.append(pelicula.titulo + " , Puntuacion media: " + str(i[1]))
    return render_to_response('peliculasPuntuadas.html', {'peliculasPuntuadas':peliculasPuntuadas})

def peliculasAno(request):
    peliculas = []
    conn = sqlite3.connect('movielens.db')

    if request.method=='POST':
        formulario = PeliculasAnoForm(request.POST)
        if formulario.is_valid():
            ano = formulario.cleaned_data['ano']
            tmp = str(ano)
            cursor = conn.execute("""SELECT id from principal_pelicula where strftime('%Y', fechaEstreno) like ?;""", (tmp,))

            for i in cursor:
                pelicula = Pelicula.objects.get(pk=i[0])
                peliculas.append(pelicula)
            return render_to_response('peliculas.html', {'peliculas': peliculas})
    else:
        formulario = PeliculasAnoForm()
        return render_to_response('formpeliculas.html',{'formulario':formulario}, context_instance=RequestContext(request))

def peliculasPuntuadasPorUsuario(request):
    
    peliculas = []
    conn = sqlite3.connect('movielens.db')

    if request.method=='POST':
        formulario = PeliculasPuntutadasUsuarioForm(request.POST)
        if formulario.is_valid():
            idUsuario = formulario.cleaned_data['idUsuario']
            tmp = str(idUsuario)
            cursor = conn.execute("""SELECT  pelicula_id, cantidad FROM principal_puntuacion  where usuario_id = ?;""", (tmp,))

            for i in cursor:
                pelicula = Pelicula.objects.get(pk=i[0])
                peliculas.append(pelicula.titulo + " puntuacion dada: " +str(i[1]))
            return render_to_response('peliculasPuntuadasUsuario.html', {'peliculas': peliculas, 'usuario':idUsuario})
    else:
        formulario = PeliculasPuntutadasUsuarioForm()
        return render_to_response('formPeliculasUsuario.html',{'formulario':formulario}, context_instance=RequestContext(request))