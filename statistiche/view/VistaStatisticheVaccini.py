
from PyQt5 import Qt, QtGui
from PyQt5.QtChart import QPieSeries, QChart, QChartView, QPieSlice
from PyQt5.QtGui import QFont, QPainter, QColor, QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel
from PyQt5.QtCore import Qt

from statistiche.controller.ControlloreStatistiche import ControlloreStatistiche


class VistaStatisticheVaccini(QWidget):

    def __init__(self, parent=None):
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

        self.setFont(QFont('Arial Nova Light'))
        self.setWindowTitle("Statistiche Vaccini")
        self.setWindowIcon(QIcon('appuntamentovaccino/data/CovidFree_Clinica.png'))

        self.resize(950, 950)
        self.move(0, 0)

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
        self.get_torta(self.effetti_collaterali_astrazeneca, "Effetti collaterali \n Astrazeneca", 0, 1)
        self.get_torta(self.effetti_collaterali_moderna, "Effetti collaterali \n Moderna", 1, 0)
        self.get_torta(self.effetti_collaterali_pfizer, "Effetti collaterali \n Pfizer", 1, 1)
        self.setLayout(self.grid_layout)

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
                red = 100
                green = 230
                for slice in torta.slices():
                    slice.setLabel("{:.1f}%".format(100 * slice.percentage()))
                    slice.setBrush(QColor(red, green, 254))
                    red += 10
                    green -= 5
                chart = QChart()
                chart.addSeries(torta)
                chart.setAnimationOptions(QChart.SeriesAnimations)
                chart.setTitle(titolo)
                chart.setTitleFont(QFont('Arial Nova Light', 15, weight=QtGui.QFont.Bold))
                chart.setTitleBrush(QColor(160, 200, 254))
                chart.legend().setAlignment(Qt.AlignRight)
                i = 0
                for key in elenco:
                    chart.legend().markers(torta)[i].setLabel(key)
                    i+=1
                self.chartview = QChartView(chart)
                self.chartview.setRenderHint(QPainter.Antialiasing)
                self.grid_layout.addWidget(self.chartview, riga, colonna)

        if msg:
            label = QLabel("Al momento non sono ancora \n disponibili dati su " + titolo)
            font_label = label.font()
            font_label.setPointSize(12)
            font_label.setFamily('Arial Nova Light')
            label.setFont(font_label)
            label.setAlignment(Qt.AlignCenter)
            self.grid_layout.addWidget(label, riga, colonna)


