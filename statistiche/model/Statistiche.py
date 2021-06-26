import os
import pickle


class Statistiche():
    def __init__(self):
        super(Statistiche, self).__init__()
        self.elenco_appuntamenti_vaccini = []
        self.elenco_appuntamenti_tamponi = []

        if os.path.isfile('calendariovaccini/data/elenco_appuntamenti_fissati.pickle'):
            with open('calendariovaccini/data/elenco_appuntamenti_fissati.pickle', 'rb') as f:
                self.elenco_appuntamenti_vaccini = pickle.load(f)

        if os.path.isfile('calendariotamponi/data/elenco_appuntamenti_salvati.pickle'):
            with open('calendariotamponi/data/elenco_appuntamenti_salvati.pickle', 'rb') as f:
                self.elenco_appuntamenti_tamponi = pickle.load(f)

    def salva_effetti_collaterali(self,effetti_collaterali):
            with open('statistiche/data/effetti_collaterali_{}.pickle'.format(effetti_collaterali[0]), 'wb') as handle:
                effetti_collaterali.pop(0)
                pickle.dump(effetti_collaterali, handle, pickle.HIGHEST_PROTOCOL)

    def salva_dati_tamponi(self,dati_tamponi):
            with open('statistiche/data/dati_tamponi.pickle', 'wb') as handle:
                pickle.dump(dati_tamponi, handle, pickle.HIGHEST_PROTOCOL)
