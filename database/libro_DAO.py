from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_generi(self):
        cnx = DBConnect.get_connection()

        if cnx is None:
            return []

        cursor_dict = cnx.cursor(dictionary=True)

        query="SELECT genere FROM libro"
        cursor_dict.execute(query)

        generi = []
        for row in cursor_dict:
            genere= row['genere']
            generi.append(genere)

        cursor_dict.close()
        cnx.close()
        return generi

    def get_libri_filtrati(self,id_bibloteca, genere):
        cnx = DBConnect.get_connection()

        if cnx is None:
            return []

        cursor_dict = cnx.cursor(dictionary=True)

        query = """
                SELECT * 
                FROM libro 
                WHERE id_biblioteca = COALESCE(%s, id_biblioteca) 
                AND genere = COALESCE(%s, genere) 
                """

        cursor_dict.execute(query, (id_bibloteca, genere))

        libri = []

        for row in cursor_dict:
            libro=Libro(**row)
            libri.append(libro)

        cursor_dict.close()
        cnx.close()
        return libri

