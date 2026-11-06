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

        self._view.selezione_biblioteca.options.append(ft.DropdownOption(key='nessuno', text='Nessun filtro'))

        for biblioteca in biblioteche:  #scorro tutte le biblioteche
            self._view.selezione_biblioteca.options.append(ft.DropdownOption(key=str(biblioteca.id), text=biblioteca.nome))  #Aggiunge
            #ogni biblioteca alle opzioni della dropdown
        self._view.update()

    def popola_dropdown_genere(self):
        generi = self._model.get_generi()

        generi_disponibili = []
        self._view.selezione_genere.options.append(ft.DropdownOption(key='nessuno', text='Nessun filtro'))
        for genere in generi:
            if genere not in generi_disponibili:
                self._view.selezione_genere.options.append(ft.DropdownOption(text=genere))
                generi_disponibili.append(genere)

        self._view.update()
    # TODO

    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA LIBRI
    # TODO
