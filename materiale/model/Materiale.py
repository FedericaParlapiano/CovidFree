class Materiale():
    def __init__(self, tipologia, id, quantita):
        super(Materiale, self).__init__()

        self.tipologia = tipologia
        self.id = id
        self.quantita = quantita

    def is_disponibile(self):
        pass