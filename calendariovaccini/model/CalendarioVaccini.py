import os
import pickle

class CalendarioVaccini():

    def __init__(self):
        super(CalendarioVaccini, self).__init__()
        self.elenco_appuntamenti = []
        self.vaccini_presenti = []

        if os.path.isfile('calendariovaccini/data/elenco_appuntamenti_fissati.pickle'):
            with open('calendariovaccini/data/elenco_appuntamenti_fissati.pickle', 'rb') as file:
                self.elenco_appuntamenti = pickle.load(file)

    def aggiungi_appuntamento(self, appuntamento):
        self.elenco_appuntamenti.append(appuntamento)

    def get_appuntamento_by_id(self, id):
        return self.elenco_appuntamenti[id]

    def get_elenco_appuntamenti(self):
        return self.elenco_appuntamenti

    def elimina_appuntamento(self, appuntamento):
        for prenotazione in self.elenco_appuntamenti:
            if prenotazione == appuntamento:
                self.elenco_appuntamenti.remove(prenotazione)

    def save_data(self):
        with open('calendariovaccini/data/elenco_appuntamenti_fissati.pickle', 'wb') as handle:
            pickle.dump(self.elenco_appuntamenti, handle, pickle.HIGHEST_PROTOCOL)

    def lettura_magazzino(self):
        if os.path.isfile('magazzino/data/lista_vaccini_salvata.pickle'):
            with open('magazzino/data/lista_vaccini_salvata.pickle', 'rb') as f:
                self.vaccini_presenti = pickle.load(f)

    def aggiorna_magazzino(self, tipologia):
        for vaccino in self.vaccini_presenti:
            if tipologia == vaccino.tipologia:
                vaccino.quantita = vaccino.quantita + 1
                with open('magazzino/data/lista_vaccini_salvata.pickle', 'wb') as handle:
                    pickle.dump(self.vaccini_presenti, handle, pickle.HIGHEST_PROTOCOL)
