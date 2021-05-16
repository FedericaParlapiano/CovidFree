from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from CovidFree.Calendariovaccini.view.VistaCalendarioVaccino import VistaCalendarioVaccini


class VistaHome(QWidget):

    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        grid_layout = QGridLayout()

        grid_layout.addWidget(self.get_generic_button("Calendario Vaccini", "rgb(204,255,255)", self.go_calendario_vaccini), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Calendario Tamponi", "rgb(255,255,153)", self.go_calendario_tamponi), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Magazzino", "rgb(255,204,255)", self.go_magazzino), 2, 0)


        self.setLayout(grid_layout)
        self.resize(400, 300)

        self.setWindowTitle("Clinica COVID FREE")

    def get_generic_button(self, titolo, colore, on_click):
        button = QPushButton(titolo)
        button.setStyleSheet("background-color: {}".format(colore))
        button.setFont(QFont('Georgia', 10))
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_calendario_vaccini(self):
        self.vista_calendario_vaccini = VistaCalendarioVaccini()
        self.vista_calendario_vaccini.show()

    def go_calendario_tamponi(self):
        pass

    def go_magazzino(self):
        pass