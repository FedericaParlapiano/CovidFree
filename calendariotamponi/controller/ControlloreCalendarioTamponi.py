from calendariotamponi.model.CalendarioTamponi import CalendarioTamponi

class ControlloreCalendarioTamponi():
    def __init__(self):
        super(ControlloreCalendarioTamponi, self).__init__()
        self.model = CalendarioTamponi()

    def aggiungi_appuntamento(self, appuntamento):
        self.model.aggiungi_appuntamento(appuntamento)

    def get_elenco_appuntamenti(self):
        return self.model.get_elenco_appuntamenti()

    def get_appuntamento_by_id(self, id):
        return self.model.get_appuntamento_by_id(id)

    def save_data(self):
        self.model.save_data()
