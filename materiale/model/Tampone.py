from materiale.model.Materiale import Materiale


class Tampone(Materiale):
    def __init__(self, tipologia, id, quantita, scadenza, prezzo):
        super(Tampone, self).__init__(tipologia, id, quantita, scadenza)

        self.prezzo = prezzo