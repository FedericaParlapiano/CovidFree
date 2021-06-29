import os
import pickle

from calendariotamponi.model.CalendarioTamponi import CalendarioTamponi


class ControlloreCalendarioTamponi():
    def __init__(self):
        super(ControlloreCalendarioTamponi, self).__init__()
        self.model = CalendarioTamponi()

    def aggiungi_appuntamento(self, appuntamento):
        self.model.aggiungi_appuntamento(appuntamento)
        self.save_data()

    def get_elenco_appuntamenti(self):
        return self.model.get_elenco_appuntamenti()

    def get_appuntamento_by_data(self, data): #da eliminare
        return self.model.get_appuntamento_by_data(data)

    def elimina_appuntamento(self, appuntamento):
        self.model.elimina_appuntamento(appuntamento)
        self.save_data()

    def save_data(self):
        return self.model.save_data()

    def lettura_magazzino(self):
        self.model.lettura_magazzino()

    def aggiorna_magazzino(self, tipologia):
        self.model.aggiorna_magazzino(tipologia)

    def get_appuntamento(self, nome, cognome, id):
        return self.model.get_appuntamento(nome, cognome, id)