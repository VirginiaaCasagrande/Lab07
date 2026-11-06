from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_libri(self):
        cnx = DBConnect.get_connection()

        if cnx is None:
            return []

        cursor_dict = cnx.cursor(dictionary=True)

        query="SELECT genere FROM libro"
        cursor_dict.execute(query)

        generi = []
        for row in cursor_dict:
            genere= row[0]
            generi.append(genere)

        cursor_dict.close()
        cnx.close()
        return generi


    # TODO
