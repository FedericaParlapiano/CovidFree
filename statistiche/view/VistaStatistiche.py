from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QLabel, QGridLayout, QVBoxLayout

from statistiche.controller.ControlloreStatistiche import ControlloreStatistiche
from statistiche.view.VistaInserisciDatiTamponi import VistaInserisciDatiTamponi
from statistiche.view.VistaInserisciEffettiCollaterali import VistaInserisciEffettiCollaterali
from statistiche.view.VistaStatisticheTamponi import VistaStatisticheTamponi
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

        self.get_label("Vaccini", v_layout_vaccini)
        self.get_button("Inserisci dati", grid_layout_vaccini, 0, 0, "rgb(152,231,221)", self.go_inserisci_vaccini)
        self.get_button("Visualizza statistiche", grid_layout_vaccini, 1, 0, "rgb(152,231,221)", self.go_visulizza_vaccini)
        self.get_label("Tamponi", v_layout_tamponi)
        self.get_button("Inserisci dati", grid_layout_tamponi, 0, 0, "rgb(152,231,221)", self.go_inserisci_tamponi)
        self.get_button("Visualizza statistiche", grid_layout_tamponi, 1, 0, "rgb(152,231,221)", self.go_visualizza_tamponi)

        v_layout_vaccini.addLayout(grid_layout_vaccini)
        v_layout_tamponi.addLayout(grid_layout_tamponi)
        v_layout.addLayout(v_layout_vaccini)
        v_layout.addWidget(QLabel(" "))
        v_layout.addLayout(v_layout_tamponi)

        self.setLayout(v_layout)
        self.setFont(QFont('Arial Nova Light'))
        self.setWindowTitle("Statistiche")
        self.setWindowIcon(QIcon('appuntamentovaccino/data/CovidFree_Clinica.png'))

        self.setMaximumSize(500, 400)
        self.resize(500, 400)
        self.move(200, 100)

    def get_label(self, testo, layout):
        label = QLabel(testo)
        font_label = label.font()
        font_label.setPointSize(15)
        font_label.setBold(True)
        label.setFont(font_label)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

    # Funzione che viene richiamata per creare un bottone.
    def get_button(self, testo, layout, riga, colonna, colore, connect):
        button = QPushButton(testo)
        button.setFont(QFont('Arial Nova Light', 12))
        button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        button.setStyleSheet("background-color: {}" .format(colore))
        button.clicked.connect(connect)
        layout.addWidget(button, riga, colonna)

    # Funzione che mostra la vista per la visualizzazione delle statistiche sui vaccini.
    def go_visulizza_vaccini(self):
        self.vista_statistiche_vaccini = VistaStatisticheVaccini()
        self.vista_statistiche_vaccini.show()

    # Funzione che mostra la vista per l'inserimento dei dati per le statistiche sui vaccini.
    def go_inserisci_vaccini(self):
        self.inserisci_effetti_collaterali = VistaInserisciEffettiCollaterali()
        self.inserisci_effetti_collaterali.show()

    # Funzione che mostra la vista per la visualizzazione delle statistiche sui tamponi.
    def go_visualizza_tamponi(self):
        self.vista_statistiche_tamponi = VistaStatisticheTamponi()
        self.vista_statistiche_tamponi.show()

    # Funzione che mostra la vista per l'inserimento dei dati per le statistiche sui tamponi.
    def go_inserisci_tamponi(self):
        self.inserisci_dati_tamponi= VistaInserisciDatiTamponi()
        self.inserisci_dati_tamponi.show()