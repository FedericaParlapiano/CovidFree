from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QVBoxLayout, QHBoxLayout, QListView

from statistiche.controller.ControlloreStatistiche import ControlloreStatistiche


class VistaStatisticheVaccini(QWidget):

    def __init__(self, parent=None, v_layout=None):

        super(VistaStatisticheVaccini, self).__init__(parent)

        self.controller = ControlloreStatistiche()

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        button_vaccini_somministrati = QPushButton("Visualizza statistiche sui vaccini somministrati")
        button_vaccini_somministrati.setFont(QFont('Georgia', 10))
        button_vaccini_somministrati.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button_vaccini_somministrati.setStyleSheet("background-color: rgb(255,255,153)")
        button_vaccini_somministrati.clicked.connect(self.go_vaccini_somministrati)
        self.h_layout.addWidget(button_vaccini_somministrati)

        button_eff_collaterali = QPushButton("Visualizza statistiche sugli effetti collaterali")
        button_eff_collaterali.setFont(QFont('Georgia', 10))
        button_eff_collaterali.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button_eff_collaterali.setStyleSheet("background-color: rgb(255,255,153)")
        button_eff_collaterali.clicked.connect(self.go_eff_collaterali)
        self.h_layout.addWidget(button_eff_collaterali)

        self.list_view = QListView()
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.list_view)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Statistiche Vaccini")
        self.resize(450, 350)


    def go_vaccini_somministrati(self):
        pass


    def go_eff_collaterali(self):
        pass
