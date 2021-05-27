from magazzino.model.Magazzino import Magazzino


class ControlloreMagazzino():
    def __init__(self):

        super(ControlloreMagazzino, self).__init__()
        self.model = Magazzino()

    def get_presidio_by_index(self, index):
        return self.model.get_presidio_by_index(index)

    def get_magazzino(self):
        return self.model.get_magazzino()

    def save_data(self):
        self.model.save_data()