from PyQt5.QtWidgets import QWidget


class VistaInserisciAppuntamentoTampone(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciAppuntamentoTampone, self).__init__()
        self.controller = controller
        self.callback = callback
        self.info = {}



