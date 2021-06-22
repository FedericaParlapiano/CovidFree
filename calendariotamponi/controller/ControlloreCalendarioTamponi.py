import os
import pickle

from calendariotamponi.model.CalendarioTamponi import CalendarioTamponi


class ControlloreCalendarioTamponi():
    def __init__(self):
        super(ControlloreCalendarioTamponi, self).__init__()
        self.model = CalendarioTamponi()

        if os.path.isfile('calendariotamponi/data/elenco_appuntamenti_salvati.pickle'):
            with open('calendariotamponi/data/elenco_appuntamenti_salvati.pickle', 'rb') as f:
                elenco_appuntamenti_salvati = pickle.load(f)
            self.model = elenco_appuntamenti_salvati

    def aggiungi_appuntamento(self, appuntamento):
        self.model.aggiungi_appuntamento(appuntamento)
        self.save_data()

    def get_elenco_appuntamenti(self):
        return self.model.get_elenco_appuntamenti()

    def get_appuntamento_by_data(self, data):
        return self.model.get_appuntamento_by_data(data)

    def elimina_appuntamento(self, appuntamento):
        self.model.elimina_appuntamento(appuntamento)
        self.save_data()

    def save_data(self):
        with open('calendariotamponi/data/elenco_appuntamenti_salvati.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)


