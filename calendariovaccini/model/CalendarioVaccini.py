import os
import pickle

class CalendarioVaccini():
    def __init__(self):
        super(CalendarioVaccini, self).__init__()
        self.elenco_appuntamenti = []
        if os.path.isfile('calendariovaccini/data/elenco_appuntamenti_fissati.pickle'):
            with open('calendariovaccini/data/elenco_appuntamenti_fissati.pickle', 'rb') as file:
                self.elenco_appuntamenti = pickle.load(file)

    def aggiungi_appuntamento(self, appuntamento):
        self.elenco_appuntamenti.append(appuntamento)

    def get_appuntamento_by_id(self, id):
        return self.elenco_appuntamenti[id]

    def get_elenco_appuntamenti(self):
        return self.elenco_appuntamenti

    def save_data(self):
        with open('calendariovaccini/data/elenco_appuntamenti_fissati.pickle', 'wb') as handle:
            pickle.dump(self.elenco_appuntamenti, handle, pickle.HIGHEST_PROTOCOL)
