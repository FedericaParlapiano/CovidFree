import os
import pickle


class AppuntamentoVaccino():

    def __init__(self, id, cartella_paziente, data_appuntamento, fascia_oraria, is_a_domicilio):

        super(AppuntamentoVaccino, self).__init__()

        self.id = id
        self.cartella_paziente = cartella_paziente
        self.is_a_domicilio = is_a_domicilio
        self.fascia_oraria = fascia_oraria
        self.data_appuntamento = data_appuntamento

        self.vaccino = self.assegna_vaccino()

    # Funzione per l'assegnamento del vaccino: dalla lettura del magazzino si popola la lista vaccini_presenti. A partire dai suoi elementi si
    # considerano i vaccini le cui quantità sono maggiorni di 0 e che, in base all'anamnesi, possono essere somministrati al soggetto.
    # Considerando, inoltre, l'eventuale preferenza espressa dallo stesso. Scelto il vaccino da assegnare si aggiorna il magazzino.
    def assegna_vaccino(self):
        preferenza = self.cartella_paziente.preferenza
        anamnesi = self.cartella_paziente.anamnesi
        da_assegnare = None
        self.vaccini_assegnabili = []
        self.vaccini_presenti = []

        if os.path.isfile('magazzino/data/lista_vaccini_salvata.pickle'):
            with open('magazzino/data/lista_vaccini_salvata.pickle', 'rb') as f:
                self.vaccini_presenti = pickle.load(f)

        if self.vaccini_presenti:
            for vaccino in self.vaccini_presenti:
                if vaccino.is_disponibile(): self.vaccini_assegnabili.append(vaccino.tipologia)

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
                if da_assegnare == vaccino.tipologia:
                    vaccino.quantita = vaccino.quantita - 1
                    with open('magazzino/data/lista_vaccini_salvata.pickle', 'wb') as handle:
                        pickle.dump(self.vaccini_presenti, handle, pickle.HIGHEST_PROTOCOL)

        return da_assegnare