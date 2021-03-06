from principal.models import UsuarioArtista,Artista
from django.shortcuts import render_to_response
from principal.forms import ArtistasPorUsuarioForm
from django.template import RequestContext
import sqlite3
# Create your views here.

def inicio(request):
    return render_to_response('inicio.html')

def artistasPorUsuario(request):
    artistas = []
    conn = sqlite3.connect('lastFM.db')

    if request.method=='POST':
        formulario = ArtistasPorUsuarioForm(request.POST)
        if formulario.is_valid():
            usuarioId = formulario.cleaned_data['id']
            tmp = str(usuarioId)
            cursor = conn.execute("""SELECT * from principal_usuarioartista where idUsuario = ?;""", (tmp,))
            for i in cursor:
                print(i)
                artista = Artista.objects.get(pk=i[2])
                artistas.append(artista.nombre + " - Tiempo de escucha: " + i[3])
            return render_to_response('artistasPorUsuario.html', {'artistas': artistas})
    else:
        formulario = ArtistasPorUsuarioForm()
        return render_to_response('artistasPorUsuarioForm.html',{'formulario':formulario}, context_instance=RequestContext(request))

def artistasRecomendosPorUsuario(request):
    artistas = []
    conn = sqlite3.connect('lastFM.db')

    if request.method=='POST':
        formulario = ArtistasPorUsuarioForm(request.POST)
        if formulario.is_valid():
            usuarioId = formulario.cleaned_data['id']
            tmp = str(usuarioId)
            cursor = conn.execute("""SELECT * from principal_usuarioartista where idUsuario = ?;""", (tmp,))
            for i in cursor:
                print(i)
                artista = Artista.objects.get(pk=i[2])
                artistas.append(artista.nombre + " - Tiempo de escucha: " + i[3])
            return render_to_response('artistasPorUsuario.html', {'artistas': artistas})
    else:
        formulario = ArtistasPorUsuarioForm()
        return render_to_response('artistasPorUsuarioForm.html',{'formulario':formulario}, context_instance=RequestContext(request))
    
def artistasMasEscuchadosUsuario(idUsuario):
    artistas = []
    conn = sqlite3.connect('lastFM.db')
    cursor = conn.execute("""SELECT * from principal_usuarioartista where idUsuario = ? order by tiempoEscucha desc;""", (idUsuario,))
    for i in cursor:
        print(i)
        artista = Artista.objects.get(pk=i[2])
        artistas.append(artista)
    
    print artistas

artistasMasEscuchadosUsuario(1)
