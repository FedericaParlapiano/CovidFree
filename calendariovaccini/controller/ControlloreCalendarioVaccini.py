from calendariovaccini.model.CalendarioVaccini import CalendarioVaccini


class ControlloreCalendarioVaccini():
    def __init__(self):
        super(ControlloreCalendarioVaccini, self).__init__()
        self.model = CalendarioVaccini()

    def aggiungi_appuntamento(self, appuntamento):
        self.model.aggiungi_appuntamento(appuntamento)

    def get_elenco_appuntamenti(self):
        return self.model.get_elenco_appuntamenti()

    def get_appuntamento_by_id(self, id):
        return self.model.get_appuntamento_by_id(id)

    def elimina_appuntamento_by_id(self, id):
        self.model.elimina_appuntamento_by_id(id)

    def save_data(self):
        self.model.save_data()
