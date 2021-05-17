from materiale.model.Materiale import Materiale


class Vaccino(Materiale):
    def __init__(self, tipologia, id, quantita, scadenza):
        super(Vaccino, self).__init__(tipologia, id, quantita, scadenza)

        self.is_doppia_dose = False
        self.distanza_seconda_dose = 0
        self.limitazioni = None

    def verifica_doppia_dose(self):
        pass

    def calcola_distanza_seconda_dose(self):
        pass

    def imposta_limitazioni(self):
        pass
