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
        if os.path.isfile('magazzino/data/lista_vaccini_salvata.pickle'):
            with open('magazzino/data/lista_vaccini_salvata.pickle', 'rb') as f:
                self.vaccini = pickle.load(f)
        else:
            with open('magazzino/data/lista_vaccini.json') as f:
                vaccini_iniziali = json.load(f)
            for vaccino in vaccini_iniziali:
                self.aggiungi_vaccino(Vaccino(vaccino["tipologia"], vaccino["monodose"], vaccino["distanza"], vaccino["id"], vaccino["quantita"]))


    def aggiungi_vaccino(self, vaccino):
        self.vaccini.append(vaccino)

    def get_presidio_by_index(self, index):
        return self.vaccini[index]

    def get_magazzino(self):
        return self.vaccini

    def save_data(self):
        with open('magazzino/data/lista_vaccini_salvata.pickle', 'wb') as handle:
            pickle.dump(self.vaccini, handle, pickle.HIGHEST_PROTOCOL)

