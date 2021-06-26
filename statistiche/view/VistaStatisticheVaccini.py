from PyQt5 import Qt
from PyQt5.QtChart import QPieSeries, QChart, QChartView, QPieSlice
from PyQt5.QtGui import QFont, QPen, QPainter, QColor
from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QVBoxLayout, QHBoxLayout, QListView
from PyQt5.QtCore import Qt

from statistiche.controller.ControlloreStatistiche import ControlloreStatistiche


class VistaStatisticheVaccini(QWidget):

    def __init__(self, parent=None, v_layout=None):

        super(VistaStatisticheVaccini, self).__init__(parent)

        self.controller = ControlloreStatistiche()

        self.vaccino_per_tipologia = {"Astrazeneca": 0, "Moderna": 0, "Pfizer": 0}

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

        self.v_layout.addLayout(self.h_layout)


        self.setLayout(self.v_layout)
        self.setWindowTitle("Statistiche Vaccini")
        self.resize(450, 350)

        for appuntamento in self.controller.get_elenco_appuntamenti_vaccini():
            for key in self.vaccino_per_tipologia:
                if appuntamento.vaccino == key:
                    self.vaccino_per_tipologia[appuntamento.vaccino] += 1






    def go_vaccini_somministrati(self):
        torta = QPieSeries()

        for vaccino in self.vaccino_per_tipologia:
            torta.append(vaccino, self.vaccino_per_tipologia[vaccino])

        torta.setLabelsVisible()
        torta.setLabelsPosition(QPieSlice.LabelInsideHorizontal)

        colore = 50

        for slice in torta.slices():
            slice.setLabel("{:.1f}%".format(100 * slice.percentage()))
            slice.setBrush(QColor(250,150,colore))
            colore += 25

        chart = QChart()
        chart.addSeries(torta)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Vaccini somministrati")
        #chart.setTheme(QChart.ChartTheme)
        chart.legend().setAlignment(Qt.AlignBottom)
        chart.legend().markers(torta)[0].setLabel("Astrazeneca")
        chart.legend().markers(torta)[1].setLabel("Moderna")
        chart.legend().markers(torta)[2].setLabel("Pfizer")


        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        self.v_layout.addWidget(chartview)


    def go_eff_collaterali(self):
        pass
