import json
import os
import pickle

from materiale.model.Tampone import Tampone
from materiale.model.Vaccino import Vaccino


class Magazzino():
    def __init__(self):
        super(Magazzino, self).__init__()
        self.magazzino = []
        self.vaccini = []
        self.tamponi = []

        if os.path.isfile('magazzino/data/lista_vaccini_salvata.pickle'):
            with open('magazzino/data/lista_vaccini_salvata.pickle', 'rb') as f:
                self.vaccini = pickle.load(f)
        else:
            with open('magazzino/data/lista_vaccini.json') as f:
                vaccini_iniziali = json.load(f)
            for vaccino in vaccini_iniziali:
                self.aggiungi_vaccino(Vaccino(vaccino["tipologia"], vaccino["doppia dose"], vaccino["distanza"], vaccino["id"], vaccino["quantita"]))

        if os.path.isfile('magazzino/data/lista_tamponi_salvata.pickle'):
            with open('magazzino/data/lista_tamponi_salvata.pickle', 'rb') as f:
                self.tamponi = pickle.load(f)
        else:
            with open('magazzino/data/lista_tamponi.json') as f:
                tamponi_iniziali = json.load(f)
            for tampone in tamponi_iniziali:
                self.aggiungi_tampone(Tampone(tampone["tipologia"], tampone["id"], tampone["quantita"], tampone["prezzo"]))

        self.magazzino = self.vaccini + self.tamponi

    # Funzione che aggiunge alla lista dei vaccini il vaccino passato come parametro.
    def aggiungi_vaccino(self, vaccino):
        self.vaccini.append(vaccino)

    # Funzione che aggiunge alla lista dei tamponi il tampone passato come parametro.
    def aggiungi_tampone(self, tampone):
        self.tamponi.append(tampone)

    # Funzione che restituisce il presidio presente nella lista magazzino nella posizione passata come parametro.
    def get_presidio_by_index(self, index):
        return self.magazzino[index]

    # Funzione che restituisce la lista dei tamponi.
    def get_tamponi(self):
        return self.tamponi

    # Funzione che restituisce la lista dei vaccini.
    def get_vaccini(self):
        return self.vaccini

    # Funzione che restituisce il magazzino.
    def get_magazzino(self):
        return self.magazzino

    # Funzione che aggiorna la quantità del materiale passato come parametro sommando alla quantità già presente il numero passato come parametro.
    def aggiorna_quantita_by_tipologia(self, tipologia, quantita):
        for materiale in self.get_magazzino():
            if materiale.tipologia == tipologia:
                materiale.aggiorna_quantita(quantita)
        self.save_data()

    # Funzione che salva i file con i dati aggiornati.
    def save_data(self):
        with open('magazzino/data/lista_vaccini_salvata.pickle', 'wb') as handle:
            pickle.dump(self.vaccini, handle, pickle.HIGHEST_PROTOCOL)

        with open('magazzino/data/lista_tamponi_salvata.pickle', 'wb') as handle:
            pickle.dump(self.tamponi, handle, pickle.HIGHEST_PROTOCOL)
