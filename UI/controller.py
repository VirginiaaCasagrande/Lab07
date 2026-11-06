import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdown_biblioteche(self):
        biblioteche = self._model.get_biblioteche()  #recupero le biblioteche

        for biblioteca in biblioteche:  #scorro tutte le biblioteche
            self._view.selezione_biblioteca.options.append(ft.DropdownOption(key=str(biblioteca.id), text=biblioteca.nome))  #creo
            #una voce nella tendina con testo biblioteca.nome
        self._view.update()
    # TODO

    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA LIBRI
    # TODO
