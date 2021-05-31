from materiale.model.Materiale import Materiale


class Tampone(Materiale):
    def __init__(self, tipologia, id, quantita, prezzo):
        super(Tampone, self).__init__(tipologia, id, quantita)
        self.categoria = "Tampone"
        self.prezzo = prezzo