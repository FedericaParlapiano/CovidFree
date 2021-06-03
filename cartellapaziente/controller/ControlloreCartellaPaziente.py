class ControlloreCartellaaziente():
    def __init__(self, cartella_paziente):
        self.model = cartella_paziente

    def get_nome_paziente(self):
        return self.model.nome

    def get_cognome_paziente(self):
        return self.model.cognome

    def get_data_di_nascita_paziente(self):
        return self.model.data_di_nascita

    def get_indirizzo_paziente(self):
        return self.model.indirizzo

    def get_conseso_paziente(self):
        return self.model.consenso

    def get_patologie_paziente(self):
        return self.model.patologie

    def get_preferenze_paziente(self):
        return self.model.preferenze

    def get_categoria_paziente(self):
        return self.model.categoria

    def get_anamnesi_paziente(self):
        return self.model.anamnesi


