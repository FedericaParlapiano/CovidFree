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
        self.elenco_dati_tamponi = []

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

        if os.path.isfile('statistiche/data/dati_tamponi.pickle'):
            with open('statistiche/data/dati_tamponi.pickle', 'rb') as f:
                self.elenco_dati_tamponi = pickle.load(f)

    # Funzione che permette il salvataggio degli effetti collaterali passati come paramentro
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

    # Funzione che permette il salvataggio dei dati passati come parametro.
    def salva_dati_tamponi(self, dati_tamponi):
        self.elenco_dati_tamponi.append(dati_tamponi)
        with open('statistiche/data/dati_tamponi.pickle', 'wb') as handle:
            pickle.dump(self.elenco_dati_tamponi, handle, pickle.HIGHEST_PROTOCOL)

    # Funzione che aggiunge alla lista gli effetti passati come parametro.
    def aggiungi_effetti_astrazeneca(self, effetti):
        effetti.pop(0)
        self.elenco_effetti_astrazeneca.append(effetti)

    # Funzione che aggiunge alla lista gli effetti passati come parametro.
    def aggiungi_effetti_moderna(self, effetti):
        effetti.pop(0)
        self.elenco_effetti_moderna.append(effetti)

    # Funzione che aggiunge alla lista gli effetti passati come parametro.
    def aggiungi_effetti_pfizer(self, effetti):
        effetti.pop(0)
        self.elenco_effetti_pfizer.append(effetti)

    # Funzione che restituisce la lista degli effetti collaterali del vaccino passato come parametro, dopo la lettura del file ad esso associato.
    def get_effetti_collaterali(self, vaccino):
        self.elenco_effetti = []
        if os.path.isfile('statistiche/data/effetti_collaterali_{}.pickle'.format(vaccino)):
            with open('statistiche/data/effetti_collaterali_{}.pickle'.format(vaccino), 'rb') as f:
                self.elenco_effetti = pickle.load(f)
        return self.elenco_effetti

    # Funzione che restituisce l'elenco dei dati sui tamponi effettuati.
    def get_dati_tamponi(self):
        return self.elenco_dati_tamponi
