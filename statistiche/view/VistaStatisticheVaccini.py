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
        self.get_torta(self.effetti_collaterali_moderna, "Effetti collaterali Moderna", 1, 0)
        self.get_torta(self.effetti_collaterali_pfizer, "Effetti collaterali Pfizer", 1, 1)
        self.setLayout(self.grid_layout)

    def get_torta(self, elenco, titolo, riga, colonna):
        if elenco:
            torta = QPieSeries()
            for elemento in elenco:
                torta.append(elemento, elenco[elemento])
            torta.setLabelsVisible()
            torta.setLabelsPosition(QPieSlice.LabelInsideHorizontal)
            blue = 0
            for slice in torta.slices():
                slice.setLabel("{:.1f}%".format(100 * slice.percentage()))
                slice.setBrush(QColor(240, 240, blue))
                blue += 15
            chart = QChart()
            chart.addSeries(torta)
            chart.setAnimationOptions(QChart.SeriesAnimations)
            chart.setTitle(titolo)
            chart.setTitleFont(QFont('Georgia', 15, weight=QtGui.QFont.Bold))
            chart.setTitleBrush(QColor(250, 200, 0))
            chart.legend().setAlignment(Qt.AlignRight)
            i = 0
            for key in elenco:
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


