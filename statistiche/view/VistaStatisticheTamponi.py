from PyQt5 import Qt
from PyQt5.QtChart import QPieSeries, QPieSlice, QChart, QChartView
from PyQt5.QtGui import QFont, QColor, QPainter
from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt

from statistiche.controller.ControlloreStatistiche import ControlloreStatistiche


class VistaStatisticheTamponi(QWidget):

    def __init__(self, parent=None, v_layout=None):

        super(VistaStatisticheTamponi, self).__init__(parent)

        self.controller = ControlloreStatistiche()
        self.visualizzate = False


        self.tampone_per_tipologia = {"Antigenico Rapido": 0, "Molecolare": 0, "Sierologico": 0}

        self.grid_layout = QGridLayout()
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.bottoni()

        self.setLayout(self.v_layout)
        self.setWindowTitle("Statistiche Tamponi")
        self.resize(450, 600)

        for appuntamento in self.controller.get_elenco_appuntamenti_tamponi():
            for key in self.tampone_per_tipologia:
                if appuntamento.tipo_tampone == key:
                    self.tampone_per_tipologia[appuntamento.tipo_tampone] += 1

    def bottoni(self):
        button_tamponi_somministrati = QPushButton("Statistiche sui tamponi effettuati")
        button_tamponi_somministrati.setFont(QFont('Georgia', 10))
        button_tamponi_somministrati.setFixedSize(300, 70)
        button_tamponi_somministrati.setStyleSheet("background-color: rgb(140,230,180)")
        button_tamponi_somministrati.clicked.connect(self.go_tamponi_somministrati)
        self.grid_layout.addWidget(button_tamponi_somministrati,1,0)

        button_positivi = QPushButton("Statistiche sui casi risultati positivi")
        button_positivi.setFont(QFont('Georgia', 10))
        button_positivi.setFixedSize(300, 70)
        button_positivi.setStyleSheet("background-color: rgb(140,230,180)") #150,200,150
        button_positivi.clicked.connect(self.go_positivi)
        self.grid_layout.addWidget(button_positivi, 1, 1)

        self.v_layout.addLayout(self.grid_layout)

    def go_tamponi_somministrati(self):
            torta = QPieSeries()

            for tampone in self.tampone_per_tipologia:
                torta.append(tampone, self.tampone_per_tipologia[tampone])

            torta.setLabelsVisible()
            torta.setLabelsPosition(QPieSlice.LabelInsideHorizontal)

            colore = 152

            for slice in torta.slices():
                slice.setLabel("{:.1f}%".format(100 * slice.percentage()))
                slice.setBrush(QColor(152,255,colore))
                colore += 35

            chart = QChart()
            chart.addSeries(torta)
            chart.setAnimationOptions(QChart.SeriesAnimations)
            chart.setTitle("Tamponi somministrati")
            chart.legend().setAlignment(Qt.AlignBottom)
            chart.legend().markers(torta)[0].setLabel("Antigenico Rapido")
            chart.legend().markers(torta)[1].setLabel("Molecolare")
            chart.legend().markers(torta)[2].setLabel("Sierologico")

            self.chartview = QChartView(chart)
            self.chartview.setRenderHint(QPainter.Antialiasing)
            self.grid_layout.addWidget(self.chartview,0,0)



    def go_positivi(self):
        pass