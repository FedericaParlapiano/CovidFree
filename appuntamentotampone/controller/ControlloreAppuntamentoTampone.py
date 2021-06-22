class ControlloreAppuntamentoTampone():

    def __init__(self, appuntamento):
        super(ControlloreAppuntamentoTampone, self).__init__()
        self.model = appuntamento

    def get_nome(self):
        return self.model.nome

    def get_cognome(self):
        return self.model.cognome

    def get_cf(self):
        return self.model.cf

    def get_telefono(self):
        return self.model.telefono

    def get_indirizzo(self):
        return self.model.indirizzo

    def get_data_nascita(self):
        return self.model.data_nascita

    def get_fascia_oraria(self):
        return self.model.fascia_oraria

    def get_data_appuntamento(self):
        return self.model.data_appuntamento

    def get_is_drive_through(self):
        return self.model.is_drive_through

    def get_tipo_tampone(self):
        return self.model.tipo_tampone