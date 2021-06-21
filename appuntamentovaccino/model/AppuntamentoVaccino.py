import os
import pickle

class AppuntamentoVaccino():

    def __init__(self, id, cartella_paziente, is_a_domicilio):
        super(AppuntamentoVaccino, self).__init__()
        self.id = id
        self.cartella_paziente = cartella_paziente
        self.is_a_domicilio = is_a_domicilio

        self.vaccino = self.assegna_vaccino()
        self.data_orario = self.assegna_data_orario()

    def assegna_vaccino(self):
        preferenza = self.cartella_paziente.preferenza
        anamnesi = self.cartella_paziente.anamnesi

        #vaccini_assegnabili = ['Moderna','Astrazeneca','Pfizer']
        if os.path.isfile('magazzino/data/lista_vaccini_salvata.pickle'):
            with open('magazzino/data/lista_vaccini_salvata.pickle', 'rb') as f:
                self.vaccini_presenti = pickle.load(f)
        self.vaccini_assegnabili = [vaccino for vaccino in self.vaccini_presenti if vaccino.is_disponibile()]

        if anamnesi['Pfizer'] == 'Sì' and 'Pfizer' in self.vaccini_assegnabili:
            self.vaccini_assegnabili.remove('Pfizer')
        if (anamnesi['Astrazeneca'] == 'Sì' or anamnesi['Malattie'] == 'Sì') and 'Astrazeneca' in self.vaccini_assegnabili:
            self.vaccini_assegnabili.remove('Astrazeneca')
        if anamnesi['Moderna'] == 'Sì' and 'Moderna' in self.vaccini_assegnabili:
            self.vaccini_assegnabili.remove('Moderna')

        if preferenza in self.vaccini_assegnabili:
            da_assegnare = preferenza
        elif self.vaccini_assegnabili:
            da_assegnare = self.vaccini_assegnabili[0]

        for vaccino in self.vaccini_presenti:
            if da_assegnare.tipologia == vaccino.tipologia:
                vaccino.quantita = vaccino.quantita - 1
                with open('magazzino/data/lista_vaccini_salvata.pickle', 'wb') as handle:
                    pickle.dump(self.vaccini_presenti, handle, pickle.HIGHEST_PROTOCOL)

        print(da_assegnare.tipologia)
        return da_assegnare

    def assegna_data_orario(self):
        data_orario = None
        return data_orario

