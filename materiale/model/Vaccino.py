from materiale.model.Materiale import Materiale


class Vaccino(Materiale):
    def __init__(self, tipologia, monodose, distanza, id, quantita):
        super(Vaccino, self).__init__(tipologia, id, quantita)

        self.is_monodose = monodose
        self.distanza_seconda_dose = distanza
        self.limitazioni = None

    def verifica_doppia_dose(self):
        pass

    def calcola_distanza_seconda_dose(self):
        pass

    def imposta_limitazioni(self):
        pass
