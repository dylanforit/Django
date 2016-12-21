#encoding:utf-8
import sqlite3
import re

def insertaArtista():
    conn = sqlite3.connect('lastFM.db')
    conn.execute("""DELETE FROM principal_artista""")
    conn.text_factory = str
    usuarios = open('artists.dat','r')
    for u in usuarios.readlines():
        tmp = u.split('\t')
        conn.execute("""INSERT INTO principal_artista(idArtista, nombre, url, pictureURL) VALUES (?,?,?,?)""", (tmp[0], tmp[1], tmp[2], tmp[3]))
    conn.commit()
    conn.close()
    print("Artistas insertados correctamente")
    
def insertaEtiquetas():
    conn = sqlite3.connect('lastFM.db')
    conn.execute("""DELETE FROM principal_etiqueta""")
    conn.text_factory = str
    usuarios = open('tags.dat','r')
    for u in usuarios.readlines():
        tmp = u.split('\t')
        conn.execute("""INSERT INTO principal_etiqueta(idTag, tagValue) VALUES (?,?)""", (tmp[0], tmp[1]))
    conn.commit()
    conn.close()
    print("Etiquetas insertadas correctamente")
    
def insertaUsuarioArtista():
    conn = sqlite3.connect('lastFM.db')
    conn.execute("""DELETE FROM principal_usuarioartista""")
    conn.text_factory = str
    usuarios = open('user_artists.dat','r')
    for u in usuarios.readlines():
        tmp = u.split('\t')
        conn.execute("""INSERT INTO principal_usuarioartista(idUsuario, artista_id, tiempoEscucha) VALUES (?,?,?)""", (tmp[0], tmp[1], tmp[2]))
    conn.commit()
    conn.close()
    print("Usuario-Artista insertadas correctamente")
    
def insertaUsuarioEtiquetaArtista():
    conn = sqlite3.connect('lastFM.db')
    conn.execute("""DELETE FROM principal_usuarioetiquetaartista""")
    conn.text_factory = str
    usuarios = open('user_taggedartists.dat','r')
    for u in usuarios.readlines():
        tmp = u.split('\t')
        conn.execute("""INSERT INTO principal_usuarioetiquetaartista(idUsuario, artista_id, tag_id, dia, mes, ano) VALUES (?,?,?,?,?,?)""", (tmp[0], tmp[1], tmp[2],tmp[3], tmp[4], tmp[5]))
    conn.commit()
    conn.close()
    print("Usuario-Etiqueta-Artista insertadas correctamente")

def insertaUsuarioAmigos():
    conn = sqlite3.connect('lastFM.db')
    conn.execute("""DELETE FROM principal_usuarioamigo""")
    conn.text_factory = str
    usuarios = open('user_friends.dat','r')
    for u in usuarios.readlines():
        tmp = u.split('\t')
        conn.execute("""INSERT INTO principal_usuarioamigo(idUsuario, idAmigo) VALUES (?,?)""", (tmp[0], tmp[1]))
    conn.commit()
    conn.close()
    print("Usuario-Amigo insertadas correctamente")

    
if __name__ == '__main__':
    insertaArtista()
    insertaEtiquetas()
    insertaUsuarioEtiquetaArtista()
    insertaUsuarioArtista()
    insertaUsuarioAmigos()
