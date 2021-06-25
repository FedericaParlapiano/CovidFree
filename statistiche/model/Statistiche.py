import os
import pickle


class Statistiche():
    def __init__(self):
        super(Statistiche, self).__init__()
        self.elenco_appuntamenti_vaccini = []
        self.elenco_appuntamenti_tamponi = []
        self.vaccino_per_tipologia = {"Astrazeneca": 0, "Moderna": 0, "Pfizer": 0}
        self.tampone_per_tipologia = {"Antigenico Rapido": 0, "Molecolare": 0, "Sierologico": 0}

        if os.path.isfile('calendariovaccini/data/elenco_appuntamenti_fissati.pickle'):
            with open('calendariovaccini/data/elenco_appuntamenti_fissati.pickle', 'rb') as f:
                self.elenco_appuntamenti_vaccini = pickle.load(f)

        if os.path.isfile('calendariotamponi/data/elenco_appuntamenti_salvati.pickle'):
            with open('calendariotamponi/data/elenco_appuntamenti_salvati.pickle', 'rb') as f:
                self.elenco_appuntamenti_tamponi = pickle.load(f)

        for appuntamento in self.elenco_appuntamenti_vaccini:
            for key in self.vaccino_per_tipologia:
                if appuntamento.vaccino == key:
                    self.vaccino_per_tipologia[appuntamento.vaccino] += 1

        for appuntamento in self.elenco_appuntamenti_tamponi:
            for key in self.tampone_per_tipologia:
                if appuntamento.tipo_tampone == key:
                    self.tampone_per_tipologia[appuntamento.tipo_tampone] += 1




