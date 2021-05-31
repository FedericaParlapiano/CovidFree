class Materiale():
    def __init__(self, tipologia, id, quantita):
        super(Materiale, self).__init__()

        self.tipologia = tipologia
        self.id = id
        self.quantita = quantita

    def aggiorna_quantita(self, quantita):
        self.quantita = int(self.quantita) + int(quantita)

    def is_disponibile(self):
        if self.quantita > 0:
            return True
        return False