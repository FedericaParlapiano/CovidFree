import os
import pickle

class CalendarioTamponi():
    def __init__(self):
        super(CalendarioTamponi, self).__init__()
        self.elenco_appuntamenti = []
        self.tamponi_presenti = []

        if os.path.isfile('calendariotamponi/data/elenco_appuntamenti_salvati.pickle'):
            with open('calendariotamponi/data/elenco_appuntamenti_salvati.pickle', 'rb') as f:
                elenco_appuntamenti_salvati = pickle.load(f)
            self.elenco_appuntamenti = elenco_appuntamenti_salvati

    def aggiungi_appuntamento(self, appuntamento):
        self.elenco_appuntamenti.append(appuntamento)

    def get_appuntamento_by_data(self, data):
        return self.elenco_appuntamenti[data]

    def get_appuntamento_by_index(self,index):
        return self.elenco_appuntamenti[index]

    def get_elenco_appuntamenti(self):
        return self.elenco_appuntamenti

    def elimina_appuntamento(self, appuntamento):
        for prenotazione in self.elenco_appuntamenti:
            if prenotazione == appuntamento:
                self.elenco_appuntamenti.remove(prenotazione)



    def lettura_magazzino(self):
        if os.path.isfile('magazzino/data/lista_tamponi_salvata.pickle'):
            with open('magazzino/data/lista_tamponi_salvata.pickle', 'rb') as f:
                self.tamponi_presenti = pickle.load(f)

    def aggiorna_magazzino(self, tipologia):
        for tampone in self.tamponi_presenti:
            if tipologia == tampone.tipologia:
                tampone.quantita = tampone.quantita + 1
                with open('magazzino/data/lista_tamponi_salvata.pickle', 'wb') as handle:
                    pickle.dump(self.tamponi_presenti, handle, pickle.HIGHEST_PROTOCOL)
