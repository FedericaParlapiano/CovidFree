from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QRadioButton, QButtonGroup, QGridLayout, QSpacerItem, \
    QSizePolicy, QPushButton, QCheckBox, QMessageBox

from statistiche.controller.ControlloreStatistiche import ControlloreStatistiche


class VistaInserisciDatiTamponi(QWidget):

    def __init__(self, parent=None):
        super(VistaInserisciDatiTamponi, self).__init__(parent)

        self.controller = ControlloreStatistiche()
        self.info = {}
        self.dati_tamponi = []

        self.v_layout = QVBoxLayout()

        font = QFont("Georgia",10)
        font.setUnderline(True)

        self.label = QLabel("Risultato Tampone:")
        self.label.setFont(font)
        self.v_layout.addWidget(self.label)

        self.positivo = QRadioButton('Positivo')
        self.negativo = QRadioButton('Negativo')

        self.bg = QButtonGroup(self)
        self.bg.addButton(self.positivo)
        self.bg.addButton(self.negativo)

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.positivo, 0, 0)
        grid_layout.addWidget(self.negativo, 0, 1)
        self.v_layout.addLayout(grid_layout)

        #self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        #if self.positivo.isChecked():
        self.sintomi = QLabel("Se positivo, presenta Sintomi?")
        self.sintomi.setFont(font)
        self.v_layout.addWidget(self.sintomi)

        self.sintomatico = QRadioButton('Sì')
        self.asintomatico = QRadioButton('No')

        self.bg1 = QButtonGroup(self)
        self.bg1.addButton(self.sintomatico)
        self.bg1.addButton(self.asintomatico)

        grid_layout_1 = QGridLayout()
        grid_layout_1.addWidget(self.sintomatico, 0, 0)
        grid_layout_1.addWidget(self.asintomatico, 0, 1)
        self.v_layout.addLayout(grid_layout_1)

        conferma = QPushButton("Conferma")
        conferma.clicked.connect(self.salva_dati)
        self.v_layout.addWidget(conferma)

        self.setLayout(self.v_layout)
        self.resize(360, 200)
        self.setWindowTitle("Inserisci Dati Tamponi")



    def salva_dati(self):

        if self.positivo.isChecked() and self.bg1.checkedButton() is None:
                QMessageBox.critical(self, 'Errore', 'E\' necessario compilare entrambi i campi!', QMessageBox.Ok,
                                 QMessageBox.Ok)
        elif self.negativo.isChecked():
            self.dati_tamponi.append(self.bg.checkedButton().text())
            for key in self.info.keys():
                if self.info[key].isChecked():
                    self.dati_tamponi.append(key)
            self.controller.salva_dati_tamponi(self.dati_tamponi)
            self.close()
        elif self.positivo.isChecked():
            if self.bg1.checkedButton() is not None:
                self.dati_tamponi.append(self.bg.checkedButton().text())
                self.dati_tamponi.append(self.bg1.checkedButton().text())
                for key in self.info.keys():
                    if self.info[key].isChecked():
                        self.dati_tamponi.append(key)
                self.controller.salva_dati_tamponi(self.dati_tamponi)
                self.close()
        else:
            QMessageBox.critical(self, 'Errore', 'E\' necessario compilare entrambi i campi!', QMessageBox.Ok,
                                 QMessageBox.Ok)






