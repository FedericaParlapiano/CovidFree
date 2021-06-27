from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QCheckBox, QLabel, QSpacerItem, QSizePolicy, QVBoxLayout, QRadioButton, \
    QButtonGroup, QGridLayout, QPushButton, QMessageBox

from statistiche.controller.ControlloreStatistiche import ControlloreStatistiche


class VistaInserisciEffettiCollaterali(QWidget):

    def __init__(self, parent=None):
        super(VistaInserisciEffettiCollaterali, self).__init__(parent)

        self.controller = ControlloreStatistiche()
        self.info = {}
        self.effetti_riscontrati = []

        self.v_layout = QVBoxLayout()

        font = QFont("Georgia",10)

        self.label = QLabel("Selezionare quale vaccino è stato somministrato al paziente?")
        self.label.setFont(font)
        self.v_layout.addWidget(self.label)

        font.setUnderline(True)

        self.astrazeneca = QRadioButton('Astrazeneca')
        self.moderna = QRadioButton('Moderna')
        self.pfizer = QRadioButton('Pfizer')

        self.bg = QButtonGroup(self)
        self.bg.addButton(self.astrazeneca)
        self.bg.addButton(self.moderna)
        self.bg.addButton(self.pfizer)

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.astrazeneca, 0, 0)
        grid_layout.addWidget(self.moderna, 0, 1)
        grid_layout.addWidget(self.pfizer, 0, 2)
        self.v_layout.addLayout(grid_layout)

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.molto_comuni = QLabel("Effetti collaterali molto comuni:")
        self.molto_comuni.setFont(font)
        self.v_layout.addWidget(self.molto_comuni)

        self.definisci_effetto_collaterale("Dolore al sito","Dolore nel sito di iniezione")
        self.definisci_effetto_collaterale("Arrossamento al sito","Arrossamento nel sito di iniezione")
        self.definisci_effetto_collaterale("Stanchezza","Stanchezza")
        self.definisci_effetto_collaterale("Brividi","Brividi")
        self.definisci_effetto_collaterale("Dolori","Dolori muscolari e/o articolari")
        self.definisci_effetto_collaterale("Mal di testa","Mal di testa")
        self.definisci_effetto_collaterale("Febbre","Febbre")
        self.definisci_effetto_collaterale("Nausea","Nausea")
        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.comuni = QLabel("Effetti collaterali comuni:")
        self.comuni.setFont(font)
        self.v_layout.addWidget(self.comuni)

        self.definisci_effetto_collaterale("Malessere","Sensazione di malessere")
        self.definisci_effetto_collaterale("Eruzione cutanea","Eruzione cutanea nel sito di iniezione")
        self.definisci_effetto_collaterale("Urticaria","Urticaria nel sito di iniezione")
        self.definisci_effetto_collaterale("Vomito","Vomito e/o diarrea")
        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.rari = QLabel("Effetti collaterali rari:")
        self.rari.setFont(font)
        self.v_layout.addWidget(self.rari)

        self.definisci_effetto_collaterale("Paralisi","Paralisi facciale periferica acuta")
        self.definisci_effetto_collaterale("Linfonodi","Gonfiore dei linfonodi")
        self.definisci_effetto_collaterale("Trombosi","Trombosi artriosa")
        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.definisci_effetto_collaterale("Nessun effetto", "Nessun effetto collaterale")

        conferma = QPushButton("Conferma")
        conferma.clicked.connect(self.salva_dati)
        self.v_layout.addWidget(conferma)

        self.setLayout(self.v_layout)
        self.resize(300,600)
        self.setWindowTitle("Inserisci Effetti Collaterali")

    def definisci_effetto_collaterale(self, effetto, descrizione):
        checkbox = QCheckBox(descrizione)
        self.info[effetto] = checkbox
        self.v_layout.addWidget(checkbox)

    def salva_dati(self):
        if self.bg.checkedButton() is None:
            QMessageBox.critical(self, 'Errore', 'E\' necessario indicare quale vaccino è stato somministrato '
                      'al paziente per poter procedere all\'inserimento', QMessageBox.Ok,QMessageBox.Ok)
        else:
            self.effetti_riscontrati.append(self.bg.checkedButton().text())
            for key in self.info.keys():
                if self.info[key].isChecked():
                    self.effetti_riscontrati.append(key)

            self.controller.salva_effetti_collaterali(self.effetti_riscontrati)
            self.close()
