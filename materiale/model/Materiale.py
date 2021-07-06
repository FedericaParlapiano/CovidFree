class Materiale():
    def __init__(self, tipologia, id, quantita):
        super(Materiale, self).__init__()

        self.tipologia = tipologia
        self.id = id
        self.quantita = quantita

    # Funzione che viene richiamata per aggiornare la quantià di un materiale presente nel magazzino
    def aggiorna_quantita(self, quantita):
        self.quantita = int(self.quantita) + int(quantita)

    # Funzione che verifica la disponibilità di un materiale presente nel magazzino.
    def is_disponibile(self):
        if self.quantita > 0:
            return True
        return False