import os
import pickle


class Statistiche():
    def __init__(self):
        super(Statistiche, self).__init__()
        self.elenco_appuntamenti_vaccini = []
        self.elenco_appuntamenti_tamponi = []
        self.elenco_effetti_astrazeneca = []
        self.elenco_effetti_moderna = []
        self.elenco_effetti_pfizer = []

        if os.path.isfile('calendariovaccini/data/elenco_appuntamenti_fissati.pickle'):
            with open('calendariovaccini/data/elenco_appuntamenti_fissati.pickle', 'rb') as f:
                self.elenco_appuntamenti_vaccini = pickle.load(f)

        if os.path.isfile('calendariotamponi/data/elenco_appuntamenti_salvati.pickle'):
            with open('calendariotamponi/data/elenco_appuntamenti_salvati.pickle', 'rb') as f:
                self.elenco_appuntamenti_tamponi = pickle.load(f)

        if os.path.isfile('statistiche/data/effetti_collaterali_astrazeneca.pickle'):
            with open('statistiche/data/effetti_collaterali_astrazeneca.pickle', 'rb') as f:
                self.elenco_effetti_astrazeneca = pickle.load(f)

        if os.path.isfile('statistiche/data/effetti_collaterali_moderna.pickle'):
            with open('statistiche/data/effetti_collaterali_moderna.pickle', 'rb') as f:
                self.elenco_effetti_moderna = pickle.load(f)

        if os.path.isfile('statistiche/data/effetti_collaterali_pfizer.pickle'):
            with open('statistiche/data/effetti_collaterali_pfizer.pickle', 'rb') as f:
                self.elenco_effetti_pfizer = pickle.load(f)

    def salva_effetti_collaterali(self, effetti_collaterali):
        with open('statistiche/data/effetti_collaterali_{}.pickle'.format(effetti_collaterali[0]), 'wb') as handle:
            if effetti_collaterali[0] == "Astrazeneca":
                self.aggiungi_effetti_astrazeneca(effetti_collaterali)
                pickle.dump(self.elenco_effetti_astrazeneca, handle, pickle.HIGHEST_PROTOCOL)
            elif effetti_collaterali[0] == "Moderna":
                self.aggiungi_effetti_moderna(effetti_collaterali)
                pickle.dump(self.elenco_effetti_moderna, handle, pickle.HIGHEST_PROTOCOL)
            elif effetti_collaterali[0] == "Pfizer":
                self.aggiungi_effetti_pfizer(effetti_collaterali)
                pickle.dump(self.elenco_effetti_pfizer, handle, pickle.HIGHEST_PROTOCOL)

    def salva_dati_tamponi(self,dati_tamponi):
        with open('statistiche/data/dati_tamponi.pickle', 'wb') as handle:
            pickle.dump(dati_tamponi, handle, pickle.HIGHEST_PROTOCOL)

    def aggiungi_effetti_astrazeneca(self, effetti):
        effetti.pop(0)
        self.elenco_effetti_astrazeneca.append(effetti)

    def aggiungi_effetti_moderna(self, effetti):
        effetti.pop(0)
        self.elenco_effetti_moderna.append(effetti)

    def aggiungi_effetti_pfizer(self, effetti):
        effetti.pop(0)
        self.elenco_effetti_pfizer.append(effetti)

    def get_effetti_collaterali(self, vaccino):
        if os.path.isfile('statistiche/data/effetti_collaterali_{}.pickle'.format(vaccino)):
            with open('statistiche/data/effetti_collaterali_{}.pickle'.format(vaccino), 'rb') as f:
                self.elenco_effetti = pickle.load(f)
        return self.elenco_effetti
