class AppuntamentoVaccino():
    def __init__(self, data, orario, cartella_paziente, is_a_domicilio):
        super(AppuntamentoVaccino, self).__init__()

        self.data = data
        self.orario = orario
        self.cartella_paziente = cartella_paziente
        self.is_a_domicilio = is_a_domicilio

        self.vaccino = self.assegna_vaccino()

    def assegna_vaccino(self):
        da_assegnare = None
        return da_assegnare
