class ControlloreAppuntamentoVaccino():

    def __init__(self, appuntamento_vaccino):
        self.model = appuntamento_vaccino

    def get_data_appuntamento(self):
        return self.model.data

    def get_orario_appuntamento(self):
        return self.model.orario

    def get_cartella_paziente_appuntamento(self):
        return self.model.cartella_paziente

    def get_vaccino_appuntamento(self):
        return self.model.vaccino

    def get_is_a_domicilio_appuntamento(self):
            return self.model.is_a_domicilio
