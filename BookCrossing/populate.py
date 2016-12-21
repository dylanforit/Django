#encoding:utf-8
import sqlite3
import re

def insertaUsuario():
    conn = sqlite3.connect('bookCrossing.db')
    conn.execute("""DELETE FROM principal_usuario""")
    conn.text_factory = str
    usuarios = open('BX-Users.csv','r')
    for u in usuarios.readlines():
        tmp = u.split(';')
        conn.execute("""INSERT INTO principal_usuario(idUsuario, localizacion, edad) VALUES (?,?,?)""",(cleanString(tmp[0]),cleanString(tmp[1].decode('cp1252').encode('utf-8')),cleanString(tmp[2].decode('cp1252').encode('utf-8'))))
    conn.commit()
    conn.close()
    print("Usuarios insertados")

def insertaLibro():
    conn = sqlite3.connect('bookCrossing.db')
    conn.execute("""DELETE FROM principal_libro""")
    conn.text_factory = str
    libros = open('BX-Books.csv','r')
    for l in libros.readlines():
        tmp = l.split(';')
        conn.execute("""INSERT INTO principal_libro(ISBN,titulo,autor,publicacion,editor,urlS,urlM,urlL) VALUES(?,?,?,?,?,?,?,?)""",
                     (cleanString(tmp[0]),cleanString(tmp[1].decode('cp1252').encode('utf-8')),cleanString(tmp[2].decode('cp1252').encode('utf-8')),cleanString(tmp[3]),cleanString(tmp[4].decode('cp1252').encode('utf-8')),cleanString(tmp[5]),cleanString(tmp[6]),cleanString(tmp[7])))
    conn.commit()
    conn.close()
    print("Libros insertados")


def insertaPuntuacion():
    conn = sqlite3.connect('bookCrossing.db')
    conn.execute("""DELETE FROM principal_puntuacion""")
    conn.text_factory = str
    puntuaciones = open('BX-Book-Ratings.csv', 'r')
    id=0
    for p in puntuaciones.readlines():
        tmp = p.split(';')
        conn.execute("""INSERT INTO principal_puntuacion (usuario_id,libro_id,puntuacion) VALUES (?,?,?,?)""",(id ,cleanString(tmp[0]),cleanString(tmp[1]),cleanString(tmp[2])))
        id=id+1
    conn.commit()
    conn.close()
    print("Puntuaciones insertadas")


def cleanString(texto):
    result =re.sub(r"[\"]", "", texto)
    return result


if __name__ == '__main__':
    insertaUsuario()
    insertaLibro()
    insertaPuntuacion()
