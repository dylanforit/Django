import sqlite3
from datetime import datetime

def insertaOcupacion():
    conn = sqlite3.connect('movielens.db')
    conn.execute("""DELETE FROM principal_ocupacion""")
    conn.text_factory = str
    ocupaciones = open('u.occupation', 'r')
    for u in ocupaciones.readlines():
        conn.execute("""INSERT INTO principal_ocupacion (nombre) VALUES (?)""",(u,))
    conn.commit()
    conn.close()
    
def insertaCategoria():
    conn = sqlite3.connect('movielens.db')
    conn.execute("""DELETE FROM principal_categoria""")
    conn.text_factory = str
    categorias = open('u.genre', 'r')
    for c in categorias.readlines():
        aux = c.split('|')
        if len(aux)==2:
            conn.execute("""INSERT INTO principal_categoria (idCategoria,nombre) VALUES (?,?)""",(aux[1],aux[0],))
        else:
            pass
    conn.commit()
    conn.close()

def insertaPelicula():
    ids_categorias = []
    conn = sqlite3.connect('movielens.db')
    conn.execute("""DELETE FROM principal_pelicula""")
    conn.execute("""DELETE FROM principal_pelicula_categoria""")
    conn.text_factory = str
    peliculas = open('u.item', 'r')
    for p in peliculas.readlines():
        aux = p.split('|')
        for i in range(5,24):
            if aux[i]==str(1):
                ids_categorias.append((i-4))
        conn.execute("""INSERT INTO principal_pelicula (idPelicula,titulo, fechaEstreno, imdbURL) VALUES (?,?,?,?)""",
                     (aux[0],aux[1],convierteFecha(aux[2]),aux[4]))
        for id in ids_categorias:
            conn.execute("""INSERT INTO principal_pelicula_categoria (pelicula_id, categoria_id) VALUES (?,?)""",
                         (aux[0], id))
        ids_categorias=[]


    conn.commit()
    conn.close()
    
def convierteFecha(fecha):
    aux = fecha.split('-')
    date_object = ''
    if len(aux)==3:
        fecha = aux[1]+' '+aux[0]+' '+aux[2]
        date_object = datetime.strptime(fecha, '%b %d %Y')
    return date_object
    
def main():
    insertaOcupacion()
    insertaCategoria()
    insertaPelicula()
    
if __name__ == "__main__":
    main()
