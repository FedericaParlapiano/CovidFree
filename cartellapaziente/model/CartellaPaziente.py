class CartellaPaziente():
    def __init__(self, nome, cognome, data_di_nascita, cf, indirizzo, telefono, preferenza):
        super(CartellaPaziente, self).__init__()

        self.nome = nome
        self.cognome = cognome
        self.data_di_nascita = data_di_nascita
        self.cf = cf
        self.inidirizzo = indirizzo
        #self.patologie = patologie
        self.telefono = telefono
        self.preferenza = preferenza
        #self.categoria = self.assegna_categoria()

    def assegna_categoria(self):
        categoria = None
        return categoria
