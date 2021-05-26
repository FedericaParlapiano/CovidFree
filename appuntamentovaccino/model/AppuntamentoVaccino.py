class AppuntamentoVaccino():

    def __init__(self, cartella_paziente, is_a_domicilio):
        super(AppuntamentoVaccino, self).__init__()

        self.cartella_paziente = cartella_paziente
        self.is_a_domicilio = is_a_domicilio

        self.vaccino = self.assegna_vaccino()
        self.data_orario = self.assegna_data_orario()

    def assegna_vaccino(self):
        '''
        anamnesi = self.cartella_paziente.anamnesi()

        if anamnesi['Pfizer'] == 'Sì' and anamnesi['Astrazeneca']=='Sì':
            da_assegnare = 'Moderna'
        if anamnesi['Moderna'] == 'Sì' and anamnesi['Astrazeneca']=='Sì':
            da_assegnare = 'Astrazeneca'
        if anamnesi['Pfizer'] == 'Sì' and anamnesi['Moderna']=='Sì':
            da_assegnare = 'Astrazeneca'
        if anamnesi['Pfizer'] == 'Sì' and anamnesi['Astrazeneca']=='Sì':
            da_assegnare = 'Moderna'

        return da_assegnare
        '''
        da_assegnare = None
        return da_assegnare

    def assegna_data_orario(self):
        data_orario = None
        return data_orario

