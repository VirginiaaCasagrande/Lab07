from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_biblioteche(self):
        cnx = DBConnect.get_connection()

        if cnx is None:
            return []

        cursor_dict = cnx.cursor(dictionary=True)

        query = "SELECT * FROM biblioteca"
        cursor_dict.execute(query)

        biblioteche = []

        for row in cursor_dict:
            biblioteca = Biblioteca (**row)
            biblioteche.append(biblioteca)

        cursor_dict.close()
        cnx.close()
        return biblioteche

    # TODO
