from PyQt5 import Qt, QtGui
from PyQt5.QtChart import QPieSeries, QChart, QChartView, QPieSlice, QPercentBarSeries
from PyQt5.QtGui import QFont, QPen, QPainter, QColor
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QSizePolicy, QLabel
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
        #self.bottoni()
        #self.setLayout(self.v_layout)
        self.setWindowTitle("Statistiche Vaccini")
        self.resize(1000, 1000)

        for appuntamento in self.controller.get_elenco_appuntamenti_vaccini():
            for key in self.vaccino_per_tipologia:
                if appuntamento.vaccino == key:
                    self.vaccino_per_tipologia[appuntamento.vaccino] += 1

        for lista_effetti_astrazeneca in self.controller.get_effetti_collaterali("Astrazeneca"):
            for effetto in lista_effetti_astrazeneca:
                if effetto in self.effetti_collaterali_astrazeneca:
                    self.effetti_collaterali_astrazeneca[effetto] += 1
                else:
                    self.effetti_collaterali_astrazeneca[effetto] = 1

        for lista_effetti_moderna in self.controller.get_effetti_collaterali("Moderna"):
            for effetto in lista_effetti_moderna:
                if effetto in self.effetti_collaterali_moderna:
                    self.effetti_collaterali_moderna[effetto] += 1
                else:
                    self.effetti_collaterali_moderna[effetto] = 1

        for lista_effetti_pfizer in self.controller.get_effetti_collaterali("Pfizer"):
            for effetto_p in lista_effetti_pfizer:
                if effetto_p in self.effetti_collaterali_pfizer:
                    self.effetti_collaterali_pfizer[effetto_p] += 1
                else:
                    self.effetti_collaterali_pfizer[effetto_p] = 1

        self.get_torta(self.vaccino_per_tipologia, "Vaccini somministrati", 0, 0)
        self.get_torta(self.effetti_collaterali_astrazeneca, "Effetti collaterali Astrazeneca", 0, 1)
        self.get_torta(self.effetti_collaterali_moderna, "Effetti collaterali Pfizer", 1, 0)
        self.get_torta(self.effetti_collaterali_pfizer, "Effetti collaterali Pfizer", 1, 1)
        self.setLayout(self.grid_layout)



    def bottoni(self):
        button_vaccini_somministrati = QPushButton("Statistiche sui vaccini somministrati")
        button_vaccini_somministrati.setFont(QFont('Georgia', 12))
        button_vaccini_somministrati.setFixedSize(360, 70)
        button_vaccini_somministrati.setStyleSheet("background-color: rgb(250,200,100)")
        button_vaccini_somministrati.clicked.connect(self.go_vaccini_somministrati)
        self.h_layout.addWidget(button_vaccini_somministrati)
        button_eff_collaterali = QPushButton("Statistiche sugli effetti collaterali")
        button_eff_collaterali.setFont(QFont('Georgia', 12))
        button_eff_collaterali.setFixedSize(300, 70)
        button_eff_collaterali.setStyleSheet("background-color: rgb(250,200,100)")
        button_eff_collaterali.clicked.connect(self.go_eff_collaterali)
        self.h_layout.addWidget(button_eff_collaterali)
        self.v_layout.addLayout(self.h_layout)

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
            chart.legend().markers(torta)[0].setLabel("Effetti collaterali Astrazeneca")
            chart.legend().markers(torta)[1].setLabel("Effetti collaterali Moderna")
            chart.legend().markers(torta)[2].setLabel("Effetti collaterali Pfizer")
            self.chartview = QChartView(chart)
            self.chartview.setRenderHint(QPainter.Antialiasing)
            self.grid_layout.addWidget(self.chartview, 0, 0)

    def go_eff_collaterali(self):
        self.get_torta(self.effetti_collaterali_astrazeneca, "Astrazeneca", 0, 1)
        self.get_torta(self.effetti_collaterali_moderna, "Moderna", 1, 0)
        self.get_torta(self.effetti_collaterali_pfizer, "Pfizer", 1, 1)
        self.v_layout.addLayout(self.grid_layout)

    def get_torta(self, elenco_effetti, titolo, riga, colonna):
        if elenco_effetti:
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
            chart.setTitle(titolo)
            chart.setTitleFont(QFont('Georgia', 15, weight=QtGui.QFont.Bold))
            chart.setTitleBrush(QColor(250, 200, 0))
            chart.legend().setAlignment(Qt.AlignRight)
            i = 0
            for key in elenco_effetti:
                chart.legend().markers(torta)[i].setLabel(key)
                i+=1
            self.chartview = QChartView(chart)
            self.chartview.setRenderHint(QPainter.Antialiasing)
            self.grid_layout.addWidget(self.chartview, riga, colonna)
        else:
            label = QLabel("Al momento non sono ancora \n disponibili dati su " + titolo)
            font_label = label.font()
            font_label.setPointSize(12)
            font_label.setFamily('Georgia')
            font_label.setBold(True)
            label.setFont(font_label)
            label.setAlignment(Qt.AlignCenter)
            self.grid_layout.addWidget(label, riga, colonna)


