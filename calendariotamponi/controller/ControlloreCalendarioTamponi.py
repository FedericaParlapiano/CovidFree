from calendariotamponi.model.CalendarioTamponi import CalendarioTamponi


class ControlloreCalendarioTamponi():
    def __init__(self):
        super(ControlloreCalendarioTamponi, self).__init__()
        self.model = CalendarioTamponi()

    def aggiungi_appuntamento(self, appuntamento):
        self.model.aggiungi_appuntamento(appuntamento)
        self.save_data()

    def get_elenco_appuntamenti(self):
        return self.model.get_elenco_appuntamenti()

    def get_tamponi_presenti(self):
        return self.model.get_tamponi_presenti()

    def elimina_appuntamento(self, appuntamento):
        self.model.elimina_appuntamento(appuntamento)
        self.save_data()

    def save_data(self):
        return self.model.save_data()

    def lettura_magazzino(self):
        self.model.lettura_magazzino()

    def aggiorna_magazzino(self, tipologia):
        self.model.aggiorna_magazzino(tipologia)

    def prenota_tampone(self, tipologia):
        return self.model.prenota_tampone(tipologia)

    def get_appuntamento(self, nome, cognome, id):
        return self.model.get_appuntamento(nome, cognome, id)

    def get_appuntamento_by_cf(self, nome, cognome, cf, data_nascita, tipo_tampone):
        return self.model.get_appuntamento_by_cf(nome, cognome, cf, data_nascita, tipo_tampone)