class ControlloreAppuntamentoVaccino():

    def __init__(self, appuntamento):
        self.model = appuntamento

    def get_data_appuntamento(self):
        return self.model.data_appuntamento

    def get_orario_appuntamento(self):
        return self.model.fascia_oraria

    def get_cartella_paziente_appuntamento(self):
        return self.model.cartella_paziente

    def get_vaccino_appuntamento(self):
        return self.model.vaccino

    def get_is_a_domicilio_appuntamento(self):
            return self.model.is_a_domicilio

    def get_id_appuntamento(self):
        return self.model.id