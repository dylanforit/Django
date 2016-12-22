from principal.models import Etiqueta,Artista
import sqlite3
import re



def artistasMasEscuchadosUsuario(idUsuario):
    artistas = []
    conn = sqlite3.connect('../lastFM.db')
    conn.text_factory = str
    cursor = conn.execute("""SELECT * from principal_usuarioartista where idUsuario = ? order by tiempoEscucha desc limit 5;""", (idUsuario,))
    for i in cursor:
        artista = Artista.objects.filter(idArtista=i[2])
        artistas.append(artista)
    return artistas

def etiquetasMasRepetidasPorArtistas(idArtista):
    etiquetas = []
    conn = sqlite3.connect('../lastFM.db')
    conn.text_factory = str
    cursor = conn.execute("""SELECT tag_id,count(*) from principal_usuarioetiquetaartista where artista_id = ? group by tag_id order by count(*) desc limit 4;""", (idArtista,))
    for i in cursor:
        etiqueta = Etiqueta.objects.filter(idTag=i[0])
        etiquetas.append(etiqueta)
    
    return etiquetas

def etiquetasMasRepetidasPorArtistasEscuchadosPorUsuario(idUsuario):
    artistas = []
    artistas = artistasMasEscuchadosUsuario(idUsuario)
    etiquetas = []

    for a in artistas:
        etiqaux = etiquetasMasRepetidasPorArtistas(a.idArtista)
        for e in etiqaux:
            etiquetas.append(e)
    print etiquetas
def cleanString(texto):
    result =re.sub(r"[\']", "", texto)
    return result


etiquetasMasRepetidasPorArtistasEscuchadosPorUsuario(25)