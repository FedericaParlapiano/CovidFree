from calendariovaccini.model.CalendarioVaccini import CalendarioVaccini

class ControlloreCalendarioVaccini():
    def __init__(self):
        super(ControlloreCalendarioVaccini, self).__init__()
        self.model = CalendarioVaccini()

    def aggiungi_appuntamento(self, appuntamento):
        self.model.aggiungi_appuntamento(appuntamento)
        self.save_data()

    def get_elenco_appuntamenti(self):
        return self.model.get_elenco_appuntamenti()

    def get_appuntamento_by_id(self, id):
        return self.model.get_appuntamento_by_id(id)

    def elimina_appuntamento(self, appuntamento):
        self.model.elimina_appuntamento(appuntamento)
        self.save_data()

    def save_data(self):
        self.model.save_data()

    def lettura_magazzino(self):
        self.model.lettura_magazzino()

    def aggiorna_magazzino(self, tipologia):
        self.model.aggiorna_magazzino(tipologia)
