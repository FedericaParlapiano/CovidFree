from magazzino.model.Magazzino import Magazzino


class ControlloreMagazzino():
    def __init__(self):

        super(ControlloreMagazzino, self).__init__()
        self.model = Magazzino()

    def get_presidio_by_index(self, index):
        return self.model.get_presidio_by_index(index)

    def get_elenco_vaccini(self):
        return self.model.get_vaccini()

    def get_elenco_tamponi(self):
        return self.model.get_tamponi()

    def get_magazzino(self):
        return self.model.get_magazzino()

    def aggiorna_quantita_by_tipologia(self, tipologia, quantita):
        self.model.aggiorna_quantita_by_tipologia(tipologia, quantita)

    def save_data(self):
        self.model.save_data()