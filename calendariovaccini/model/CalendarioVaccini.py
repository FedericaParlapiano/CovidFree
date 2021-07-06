import os
import pickle

class CalendarioVaccini():

    def __init__(self):
        super(CalendarioVaccini, self).__init__()
        self.elenco_appuntamenti = []
        self.vaccini_presenti = []

        if os.path.isfile('calendariovaccini/data/elenco_appuntamenti_fissati.pickle'):
            with open('calendariovaccini/data/elenco_appuntamenti_fissati.pickle', 'rb') as file:
                self.elenco_appuntamenti = pickle.load(file)

    # Funzione che appende alla lista degli appuntamenti fissati i nuovi appuntamenti che vengono inseriti.
    def aggiungi_appuntamento(self, appuntamento):
        self.elenco_appuntamenti.append(appuntamento)

    # Funzione che restituisce un appuntamento dalla lista di quelli fissati, utilizzando come parametri il nome, il cognome e il codice fiscale.
    def get_appuntamento(self, nome, cognome, id):
        for appuntamento in self.elenco_appuntamenti:
            if appuntamento.cartella_paziente.nome == nome and appuntamento.cartella_paziente.cognome == cognome and appuntamento.id == id:
                return appuntamento
        return None

    # Funzione che restituisce un appuntamento dalla lista di quelli fissati, utilizzando come parametri il nome, il cognome, il codice fiscale
    # e l'id.
    def get_appuntamento_by_cf(self, nome, cognome, cf, id):
        for appuntamento in self.elenco_appuntamenti:
            if appuntamento.cartella_paziente.nome == nome and appuntamento.cartella_paziente.cognome == cognome and appuntamento.cartella_paziente.cf == cf and appuntamento.id == id:
                return appuntamento
        return None

    # Funzione che restituisce l'elenco degli appuntamenti fissati.
    def get_elenco_appuntamenti(self):
        return self.elenco_appuntamenti

    # Funzione che elimina l'appuntamento passato come parametro dalla lista degli appuntamenti.
    def elimina_appuntamento(self, appuntamento):
        for prenotazione in self.elenco_appuntamenti:
            if prenotazione.cartella_paziente.cf == appuntamento.cartella_paziente.cf and appuntamento.vaccino == prenotazione.vaccino and prenotazione.data_appuntamento == appuntamento.data_appuntamento and prenotazione.id == appuntamento.id and prenotazione.data_appuntamento==appuntamento.data_appuntamento and prenotazione.fascia_oraria==appuntamento.fascia_oraria:
                self.elenco_appuntamenti.remove(prenotazione)
                self.aggiorna_magazzino(appuntamento.vaccino)
                return

    # Funzione per il salvataggio della lista degli appuntamenti.
    def save_data(self):
        with open('calendariovaccini/data/elenco_appuntamenti_fissati.pickle', 'wb') as handle:
            pickle.dump(self.elenco_appuntamenti, handle, pickle.HIGHEST_PROTOCOL)

    # Funzione per la lettura dei materiali presenti nel magazzino.
    def lettura_magazzino(self):
        if os.path.isfile('magazzino/data/lista_vaccini_salvata.pickle'):
            with open('magazzino/data/lista_vaccini_salvata.pickle', 'rb') as f:
                self.vaccini_presenti = pickle.load(f)

    # Funzione che viene richiamata dopo l'eliminazione di un appuntamento per aggiornare la quantità del materiale assegnato.
    def aggiorna_magazzino(self, tipologia):
        for vaccino in self.vaccini_presenti:
            if tipologia == vaccino.tipologia:
                vaccino.quantita = vaccino.quantita + 1
                with open('magazzino/data/lista_vaccini_salvata.pickle', 'wb') as handle:
                    pickle.dump(self.vaccini_presenti, handle, pickle.HIGHEST_PROTOCOL)
