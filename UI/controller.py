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
                self._view.selezione_genere.options.append(ft.DropdownOption(key=genere, text=genere))
                generi_disponibili.append(genere)

        self._view.update()

    # CALLBACKS DROPDOWN
    def handler_selezione_biblioteca(self,e):
        self.biblioteca_selezionata = e.control.value

        if self.biblioteca_selezionata == 'nessuno':
            self.biblioteca_selezionata = None

        else:
            self.biblioteca_selezionata = int(self.biblioteca_selezionata)

    def handler_selezione_genere(self,e):
        self.genere_selezionato= e.control.value

        if self.genere_selezionato == 'nessuno':
            self.genere_selezionato = None


    # AZIONE: MOSTRA LIBRI
    def handler_mostra_libri(self,e):
        id_biblioteca = self._view.selezione_biblioteca.value
        genere = self._view.selezione_genere.value

        if id_biblioteca=='nessuno':
            id_biblioteca = None

        if genere == 'nessuno':
            genere = None

        libri = self._model.get_libri_filtrati(id_biblioteca, genere)  #Recupero dal Model i libri filtrati

        self._view.list_view_libri.controls.clear()

        if len(libri)==0:
            self._view.alert.show_alert('Nessun libro trovato')

        else:
            for libro in libri:
                self._view.list_view_libri.controls.append(ft.Text(str(libro)))

        self._view.update()

