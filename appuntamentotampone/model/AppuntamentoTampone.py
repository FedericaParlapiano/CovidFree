class AppuntamentoTampone():

    def __init__(self, nome, cognome, cf, telefono, indirizzo, data_nascita, data_appuntamento, fascia_oraria, is_drive_through, tipo_tampone):
        super(AppuntamentoTampone, self).__init__()

        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.telefono = telefono
        self.indirizzo = indirizzo
        self.data_nascita = data_nascita
        self.fascia_oraria = fascia_oraria
        self.data_appuntamento = data_appuntamento
        self.is_drive_through = is_drive_through
        self.tipo_tampone = tipo_tampone

