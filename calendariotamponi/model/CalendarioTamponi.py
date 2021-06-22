import os
import pickle

class CalendarioTamponi():
    def __init__(self):
        super(CalendarioTamponi, self).__init__()
        self.elenco_appuntamenti = []

        if os.path.isfile('calendariotamponi/data/elenco_appuntamenti_salvati.pickle'):
            with open('calendariotamponi/data/elenco_appuntamenti_salvati.pickle', 'rb') as f:
                elenco_appuntamenti_salvati = pickle.load(f)
            self.elenco_appuntamenti = elenco_appuntamenti_salvati

    def aggiungi_appuntamento(self, appuntamento):
        self.elenco_appuntamenti.append(appuntamento)

    def get_appuntamento_by_data(self, data):
        return self.elenco_appuntamenti[data]

    def get_elenco_appuntamenti(self):
        return self.elenco_appuntamenti
