from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QSizePolicy, QLabel, QGridLayout, QVBoxLayout, \
    QSpacerItem

from statistiche.controller.ControlloreStatistiche import ControlloreStatistiche
from statistiche.view.VistaInserisciEffettiCollaterali import VistaInserisciEffettiCollaterali
from statistiche.view.VistaStatisticheVaccini import VistaStatisticheVaccini


class VistaStatistiche(QWidget):

    def __init__(self, parent=None):

        super(VistaStatistiche, self).__init__(parent)

        self.controller = ControlloreStatistiche()

        v_layout_vaccini = QVBoxLayout()
        v_layout_tamponi = QVBoxLayout()
        grid_layout_vaccini = QGridLayout()
        grid_layout_tamponi = QGridLayout()
        v_layout = QVBoxLayout()

        label_vaccini = QLabel("Vaccini")
        font_label_vaccini = label_vaccini.font()
        font_label_vaccini.setPointSize(15)
        font_label_vaccini.setFamily('Georgia')
        font_label_vaccini.setBold(True)
        label_vaccini.setFont(font_label_vaccini)
        label_vaccini.setAlignment(Qt.AlignCenter)
        v_layout_vaccini.addWidget(label_vaccini)

        button_vaccini_v = QPushButton("Visualizza statistiche")
        button_vaccini_v.setFont(QFont('Georgia', 10))
        button_vaccini_v.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        button_vaccini_v.setStyleSheet("background-color: rgb(255,255,153)")
        button_vaccini_v.clicked.connect(self.go_visulizza_vaccini)
        button_vaccini_i = QPushButton("Inserisci dati")
        button_vaccini_i.setFont(QFont('Georgia', 10))
        button_vaccini_i.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        button_vaccini_i.setStyleSheet("background-color: rgb(255,255,153)")
        button_vaccini_i.clicked.connect(self.go_inserisci_vaccini)

        label_tamponi = QLabel("Tamponi")
        font_label_tamponi = label_tamponi.font()
        font_label_tamponi.setPointSize(15)
        font_label_tamponi.setFamily('Georgia')
        font_label_tamponi.setBold(True)
        label_tamponi.setFont(font_label_tamponi)
        label_tamponi.setAlignment(Qt.AlignCenter)
        v_layout_tamponi.addWidget(label_tamponi)

        button_tamponi_v = QPushButton("Visualizza statistiche")
        button_tamponi_v.setFont(QFont('Georgia', 10))
        button_tamponi_v.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        button_tamponi_v.setStyleSheet("background-color: rgb(152,255,152)")
        button_tamponi_v.clicked.connect(self.go_visualizza_tamponi)
        button_tamponi_i = QPushButton("Inserisci dati")
        button_tamponi_i.setFont(QFont('Georgia', 10))
        button_tamponi_i.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        button_tamponi_i.setStyleSheet("background-color: rgb(152,255,152)")
        button_tamponi_i.clicked.connect(self.go_inserisci_tamponi)

        grid_layout_vaccini.addWidget(button_vaccini_v, 1, 0)
        grid_layout_vaccini.addWidget(button_vaccini_i, 0, 0)
        grid_layout_tamponi.addWidget(button_tamponi_v, 1, 0)
        grid_layout_tamponi.addWidget(button_tamponi_i, 0, 0)

        v_layout_vaccini.addLayout(grid_layout_vaccini)
        v_layout_tamponi.addLayout(grid_layout_tamponi)
        v_layout.addLayout(v_layout_vaccini)
        v_layout.addWidget(QLabel(" "))
        v_layout.addLayout(v_layout_tamponi)

        self.setLayout(v_layout)
        self.setWindowTitle("Statistiche")
        self.resize(450, 350)

    def go_visulizza_vaccini(self):
        self.vista_statistiche_vaccini = VistaStatisticheVaccini()
        self.vista_statistiche_vaccini.show()

    def go_inserisci_vaccini(self):
        self.inserisci_effetti_collaterali = VistaInserisciEffettiCollaterali()
        self.inserisci_effetti_collaterali.show()

    def go_visualizza_tamponi(self):
        pass

    def go_inserisci_tamponi(self):
        pass