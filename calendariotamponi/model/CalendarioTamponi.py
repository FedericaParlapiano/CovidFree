import os
import pickle

class CalendarioTamponi():
    def __init__(self):
        super(CalendarioTamponi, self).__init__()
        self.elenco_appuntamenti = []
        self.tamponi_presenti = []

        if os.path.isfile('calendariotamponi/data/elenco_appuntamenti_salvati.pickle'):
            with open('calendariotamponi/data/elenco_appuntamenti_salvati.pickle', 'rb') as f:
                self.elenco_appuntamenti = pickle.load(f)

    # Funzione che appende alla lista degli appuntamenti fissati i nuovi appuntamenti che vengono inseriti.
    def aggiungi_appuntamento(self, appuntamento):
        self.elenco_appuntamenti.append(appuntamento)

    # Funzione che restituisce l'elenco degli appuntamenti fissati.
    def get_elenco_appuntamenti(self):
        return self.elenco_appuntamenti

    # Funzione che elimina l'appuntamento passato come parametro dalla lista degli appuntamenti.
    def elimina_appuntamento(self, appuntamento):
        for prenotazione in self.elenco_appuntamenti:
            if prenotazione == appuntamento:
                self.elenco_appuntamenti.remove(prenotazione)

    # Funzione per il salvataggio della lista degli appuntamenti.
    def save_data(self):
        with open('calendariotamponi/data/elenco_appuntamenti_salvati.pickle', 'wb') as handle:
            pickle.dump(self.elenco_appuntamenti, handle, pickle.HIGHEST_PROTOCOL)

    # Funzione per la lettura dei materiali presenti nel magazzino.
    def lettura_magazzino(self):
        if os.path.isfile('magazzino/data/lista_tamponi_salvata.pickle'):
            with open('magazzino/data/lista_tamponi_salvata.pickle', 'rb') as f:
                self.tamponi_presenti = pickle.load(f)

    # Funzione che viene richiamata dopo l'eliminazione di un appuntamento per aggiornare la quantità del materiale assegnato.
    def aggiorna_magazzino(self, tipologia):
        for tampone in self.tamponi_presenti:
            if tipologia == tampone.tipologia:
                tampone.quantita = tampone.quantita + 1
                with open('magazzino/data/lista_tamponi_salvata.pickle', 'wb') as handle:
                    pickle.dump(self.tamponi_presenti, handle, pickle.HIGHEST_PROTOCOL)

    # Funzione che verifica la disponibilità del tampone richiesto per un appuntamento. In caso affermativo ne aggiorna la quantità.
    def prenota_tampone(self, tipologia):
        prenotato = False
        for tampone in self.tamponi_presenti:
            if tipologia == tampone.tipologia:
                if tampone.is_disponibile():
                    tampone.quantita = tampone.quantita - 1
                    prenotato = True
                    with open('magazzino/data/lista_tamponi_salvata.pickle', 'wb') as handle:
                        pickle.dump(self.tamponi_presenti, handle, pickle.HIGHEST_PROTOCOL)
        return prenotato

    # Funzione che restituisce un appuntamento dalla lista di quelli fissati, utilizzando come parametri il nome, il cognome e la data di nascita.
    def get_appuntamento(self, nome, cognome, data_nascita):
        for appuntamento in self.elenco_appuntamenti:
            if appuntamento.nome == nome and appuntamento.cognome == cognome and appuntamento.data_nascita == data_nascita:
                return appuntamento
        return None

    # Funzione che restituisce un appuntamento dalla lista di quelli fissati, utilizzando come parametri il nome, il cognome, la data di nascita,
    # codice fiscale e il tipo di tampone.
    def get_appuntamento_by_cf(self, nome, cognome, data_nascita, cf, tipo_tampone):
        for appuntamento in self.elenco_appuntamenti:
            if appuntamento.nome == nome and appuntamento.cognome == cognome and appuntamento.data_nascita == data_nascita and appuntamento.cf == cf \
                    and appuntamento.tipo_tampone == tipo_tampone:
                return appuntamento
        return None