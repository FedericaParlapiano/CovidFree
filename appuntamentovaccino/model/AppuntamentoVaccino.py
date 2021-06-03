class AppuntamentoVaccino():

    def __init__(self, id, cartella_paziente, is_a_domicilio):
        super(AppuntamentoVaccino, self).__init__()
        self.id = id
        self.cartella_paziente = cartella_paziente
        self.is_a_domicilio = is_a_domicilio

        self.vaccino = self.assegna_vaccino()
        self.data_orario = self.assegna_data_orario()

    def assegna_vaccino(self):

        preferenza = self.cartella_paziente.preferenza
        anamnesi = self.cartella_paziente.anamnesi

        vaccini_assegnabili = ['Moderna','Astrazeneca','Pfizer']

        if anamnesi['Pfizer'] == 'Sì':
            vaccini_assegnabili.remove('Pfizer')
        if anamnesi['Astrazeneca'] == 'Sì' or anamnesi['Malattie'] == 'Sì':
            vaccini_assegnabili.remove('Astrazeneca')
        if anamnesi['Moderna'] == 'Sì':
            vaccini_assegnabili.remove('Moderna')

        if preferenza in vaccini_assegnabili:
            da_assegnare = preferenza
        else:
            da_assegnare = vaccini_assegnabili[0]

        #manca il controllo sulla quantità
        return da_assegnare

    def assegna_data_orario(self):
        data_orario = None
        return data_orario

