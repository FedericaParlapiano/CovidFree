from PyQt5 import Qt
from PyQt5.QtChart import QPieSeries, QChart, QChartView, QPieSlice, QPercentBarSeries
from PyQt5.QtGui import QFont, QPen, QPainter, QColor
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QSizePolicy
from PyQt5.QtCore import Qt

from statistiche.controller.ControlloreStatistiche import ControlloreStatistiche


class VistaStatisticheVaccini(QWidget):

    def __init__(self, parent=None, v_layout=None):
        super(VistaStatisticheVaccini, self).__init__(parent)
        self.controller = ControlloreStatistiche()
        self.vaccino_per_tipologia = {"Astrazeneca": 0, "Moderna": 0, "Pfizer": 0}
        self.effetti_collaterali_astrazeneca = {}
        self.effetti_collaterali_moderna = {}
        self.effetti_collaterali_pfizer = {}

        self.grid_layout = QGridLayout()
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()
        self.v_layout_effetti = QHBoxLayout()
        self.bottoni()
        self.setLayout(self.v_layout)
        self.setWindowTitle("Statistiche Vaccini")
        self.resize(450, 600)

        for appuntamento in self.controller.get_elenco_appuntamenti_vaccini():
            for key in self.vaccino_per_tipologia:
                if appuntamento.vaccino == key:
                    self.vaccino_per_tipologia[appuntamento.vaccino] += 1

        for lista_effetti in self.controller.get_effetti_collaterali("Astrazeneca"):
            #print(lista_effetti)
            for effetto in lista_effetti:
                if effetto in self.effetti_collaterali_astrazeneca:
                    self.effetti_collaterali_astrazeneca[effetto] += 1
                else:
                    self.effetti_collaterali_astrazeneca[effetto] = 1

        for lista_effetti in self.controller.get_effetti_collaterali("Moderna"):
            for effetto in lista_effetti:
                if effetto in self.effetti_collaterali_moderna:
                    self.effetti_collaterali_moderna[effetto] += 1
                else:
                    self.effetti_collaterali_moderna[effetto] = 1

        for lista_effetti in self.controller.get_effetti_collaterali("Pfizer"):
            for effetto in lista_effetti:
                if effetto in self.effetti_collaterali_pfizer:
                    self.effetti_collaterali_pfizer[effetto] += 1
                else:
                    self.effetti_collaterali_pfizer[effetto] = 1

    def bottoni(self):
        button_vaccini_somministrati = QPushButton("Statistiche sui vaccini somministrati")
        button_vaccini_somministrati.setFont(QFont('Georgia', 12))
        button_vaccini_somministrati.setFixedSize(300, 70)
        button_vaccini_somministrati.setStyleSheet("background-color: rgb(250,200,100)")
        button_vaccini_somministrati.clicked.connect(self.go_vaccini_somministrati)
        self.grid_layout.addWidget(button_vaccini_somministrati,1,0)
        button_eff_collaterali = QPushButton("Statistiche sugli effetti collaterali")
        button_eff_collaterali.setFont(QFont('Georgia', 12))
        button_eff_collaterali.setFixedSize(300, 70)
        button_eff_collaterali.setStyleSheet("background-color: rgb(250,200,100)")
        button_eff_collaterali.clicked.connect(self.go_eff_collaterali)
        self.grid_layout.addWidget(button_eff_collaterali, 1, 1)
        self.v_layout.addLayout(self.grid_layout)

    def go_vaccini_somministrati(self):
            torta = QPieSeries()
            for vaccino in self.vaccino_per_tipologia:
                torta.append(vaccino, self.vaccino_per_tipologia[vaccino])
            torta.setLabelsVisible()
            torta.setLabelsPosition(QPieSlice.LabelInsideHorizontal)
            colore = 100
            for slice in torta.slices():
                slice.setLabel("{:.1f}%".format(100 * slice.percentage()))
                slice.setBrush(QColor(255,220,colore))
                colore += 40
            chart = QChart()
            chart.addSeries(torta)
            chart.setAnimationOptions(QChart.SeriesAnimations)
            chart.setTitle("Vaccini somministrati")
            chart.legend().setAlignment(Qt.AlignBottom)
            chart.legend().markers(torta)[0].setLabel("Astrazeneca")
            chart.legend().markers(torta)[1].setLabel("Moderna")
            chart.legend().markers(torta)[2].setLabel("Pfizer")
            self.chartview = QChartView(chart)
            self.chartview.setRenderHint(QPainter.Antialiasing)
            self.grid_layout.addWidget(self.chartview, 0, 0)

    def go_eff_collaterali(self):
        self.get_torta(self.effetti_collaterali_astrazeneca, "Astrazeneca")
        self.get_torta(self.effetti_collaterali_moderna, "Moderna")
        self.get_torta(self.effetti_collaterali_pfizer, "Pfizer")
        self.grid_layout.addLayout(self.v_layout_effetti, 0, 1)

    def get_torta(self, elenco_effetti, vaccino):
        torta = QPieSeries()
        for effetto in elenco_effetti:
            torta.append(effetto, elenco_effetti[effetto])
        torta.setLabelsVisible()
        torta.setLabelsPosition(QPieSlice.LabelInsideHorizontal)
        colore = 0
        for slice in torta.slices():
            slice.setLabel("{:.1f}%".format(100 * slice.percentage()))
            slice.setBrush(QColor(250, 250, colore))
            colore += 15
        chart = QChart()
        chart.addSeries(torta)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Effetti Collaterali " + vaccino)
        chart.legend().setAlignment(Qt.AlignBottom)
        i = 0
        for key in elenco_effetti:
            chart.legend().markers(torta)[i].setLabel(key)
            i+=1
        self.chartview = QChartView(chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)
        self.v_layout_effetti.addWidget(self.chartview)