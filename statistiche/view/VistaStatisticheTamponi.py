from PyQt5 import Qt, QtGui
from PyQt5.QtChart import QPieSeries, QPieSlice, QChart, QChartView
from PyQt5.QtGui import QFont, QColor, QPainter, QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt

from statistiche.controller.ControlloreStatistiche import ControlloreStatistiche


class VistaStatisticheTamponi(QWidget):

    def __init__(self, parent=None):

        super(VistaStatisticheTamponi, self).__init__(parent)

        self.controller = ControlloreStatistiche()
        self.visualizzate = False


        self.tampone_per_tipologia = {"Antigenico Rapido": 0, "Molecolare": 0, "Sierologico": 0}
        self.dati_positivi = {}
        self.dati_sintomi = {}

        self.grid_layout = QGridLayout()
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.bottoni()

        self.setLayout(self.v_layout)
        self.setFont(QFont('Arial Nova Light', 12))
        self.setWindowTitle("Statistiche Tamponi")
        self.setWindowIcon(QIcon('appuntamentovaccino/data/CovidFree_Clinica.png'))

        self.setMaximumSize(1000, 800)
        self.resize(1000, 800)
        self.move(0, 0)

        for appuntamento in self.controller.get_elenco_appuntamenti_tamponi():
            for key in self.tampone_per_tipologia:
                if appuntamento.tipo_tampone == key:
                    self.tampone_per_tipologia[appuntamento.tipo_tampone] += 1

        for lista_dati in self.controller.get_dati_tamponi():
            for dato in lista_dati:
                if dato == "Positivo":
                    if dato in self.dati_positivi:
                        self.dati_positivi[dato] += 1
                    else:
                        self.dati_positivi[dato] = 1
                elif dato == "Negativo":
                    if dato in self.dati_positivi:
                        self.dati_positivi[dato] += 1
                    else:
                        self.dati_positivi[dato] = 1
                elif dato == "Sì":
                    if "Sintomatico" in self.dati_sintomi:
                        self.dati_sintomi["Sintomatico"] += 1
                    else:
                        self.dati_sintomi["Sintomatico"] = 1
                else:
                    if "Asintomatico" in self.dati_sintomi:
                        self.dati_sintomi["Asintomatico"] += 1
                    else:
                        self.dati_sintomi["Asintomatico"] = 1

    # Funzione che viene richiamata per creare un bottone.
    def bottoni(self):
        button_tamponi_somministrati = QPushButton("Statistiche sui tamponi effettuati")
        button_tamponi_somministrati.setFixedSize(480, 70)
        button_tamponi_somministrati.setStyleSheet("background-color: rgb(150,180,255)")
        button_tamponi_somministrati.clicked.connect(self.go_tamponi_somministrati)
        self.grid_layout.addWidget(button_tamponi_somministrati, 1, 0)

        button_positivi = QPushButton("Statistiche sui casi risultati positivi")
        button_positivi.setFixedSize(480, 70)
        button_positivi.setStyleSheet("background-color: rgb(150,180,255)")
        button_positivi.clicked.connect(self.go_positivi)
        self.grid_layout.addWidget(button_positivi, 1, 1)

        button_sintomi = QPushButton("Statistiche sulla sintomatologia")
        button_sintomi.setFixedSize(480, 70)
        button_sintomi.setStyleSheet("background-color: rgb(150,180,255)")
        button_sintomi.clicked.connect(self.go_sintomi)
        self.grid_layout.addWidget(button_sintomi, 1, 2)

        self.v_layout.addLayout(self.grid_layout)

    def go_tamponi_somministrati(self):
        self.get_torta(self.tampone_per_tipologia, "Tipologia Tamponi \n effettuati", 0, 0)

    def go_positivi(self):
        self.get_torta(self.dati_positivi, "Statistiche sui casi \n risultati positivi", 0, 1)

    def go_sintomi(self):
        self.get_torta(self.dati_sintomi, "Statistiche sulla \n sintomatologia", 0, 2)

    # Funzione che, in base ai dati raccolti, crea un grafico a torta.
    def get_torta(self, elenco, titolo, riga, colonna):
        vuoto = 0
        for item in elenco:
            if elenco[item] != 0:
                vuoto += 1

        msg = True
        if vuoto:
            if elenco:
                msg = False
                torta = QPieSeries()
                for elemento in elenco:
                    torta.append(elemento, elenco[elemento])
                torta.setLabelsVisible()
                torta.setLabelsPosition(QPieSlice.LabelInsideHorizontal)

                red=120

                for slice in torta.slices():
                    slice.setLabel("{:.1f}%".format(100 * slice.percentage()))
                    slice.setBrush(QColor(red, 180, 254))
                    red += 45

                chart = QChart()
                chart.addSeries(torta)
                chart.setAnimationOptions(QChart.SeriesAnimations)
                chart.setTitle(titolo)
                chart.setTitleFont(QFont('Arial Nova Light', 15, weight=QtGui.QFont.Bold))
                chart.setTitleBrush(QColor(120,160, 254))
                chart.legend().setAlignment(Qt.AlignRight)

                i = 0
                for key in elenco:
                    chart.legend().markers(torta)[i].setLabel(key)
                    i += 1
                self.chartview = QChartView(chart)
                self.chartview.setRenderHint(QPainter.Antialiasing)
                self.grid_layout.addWidget(self.chartview, riga, colonna)

        if msg:
            label = QLabel("Al momento non sono ancora \n disponibili dati su \n" + titolo)
            label.setAlignment(Qt.AlignCenter)
            self.grid_layout.addWidget(label, riga, colonna)

