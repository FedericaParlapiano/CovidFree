class Materiale():
    def __init__(self,tipologia, id, quantita, scadenza):
        super(Materiale, self).__init__()

        self.tipologia = tipologia
        self.id = id
        self.quantita = quantita
        self.scadenza = scadenza

    def is_scaduto(self):
        pass
    def is_disponibile(self):
        pass