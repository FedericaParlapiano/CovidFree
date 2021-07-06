from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QRadioButton, QButtonGroup, QPushButton, \
     QMessageBox, QComboBox


class VistaInserisciAnamnesi(QWidget):

    def __init__(self, controller):
        super(VistaInserisciAnamnesi, self).__init__(parent=None)
        self.controller = controller

        self.info = {}
        self.anamnesi = {}

        font = QFont('Arial Nova Light', 12)
        font.setBold(True)
        self.grid_layout = QGridLayout()
        label1 = QLabel('Da compilare a cura del personale e da riesaminare insieme ai Professionisti Sanitari addetti alla vaccinazione.')
        label1.setFont(font)
        self.grid_layout.addWidget(label1, 1, 0)

        self.grid_layout.addWidget(QLabel('Soffre di allergie ad uno dei componenti del vaccino ?'), 2, 0)
        self.get_domanda('Pfizer', '- Pfizer', 3)
        self.get_domanda('Moderna', '- Moderna', 4)
        self.get_domanda('Astrazeneca', '- Astrazeneca', 5)
        self.get_domanda('Reazione grave', 'Ha mai avuto una reazione grave dopo aver ricevuto un vaccino?', 6)
        self.get_domanda('Malattie', 'Soffre di malattie cardiache o polmonari, asma, malattie renali, diabete, anemia o altre malattie del sangue?', 7)
        self.get_domanda('Sistema immunitario', 'Si trova in una condizione di compromissione del sistema immunitario (esempio: cancro, leucemia, linfoma, HIV/AIDS, trapianto)?', 8)
        self.get_domanda('Gravidanza', 'È incinta o sta pensando di rimanere incinta nel prossimo mese?', 9)

        font.setBold(False)
        font.setItalic(True)
        label2 = QLabel('Anamnesi COVID-Correlata')
        label2.setFont(font)
        self.grid_layout.addWidget(label2, 10, 0)
        self.get_domanda('Contatto', 'Nell\'ultimo mese è stato in contatto con una persona contagiata da Sars-CoV2 o affetta da COVID-19?', 11)
        self.get_domanda('Sintomi', 'Manifesta sintomi riconducibili a infezione da COVID-19?', 12)
        self.grid_layout.addWidget(QLabel('Se è stato precedentemente affetto da COVID-19, indicare quanti mesi sono trascorsi dall\'infezione'), 13, 0)
        self.mesi = QComboBox()
        self.mesi.addItems([' ', 'mai', 'meno di 3 mesi', 'tra i 3 e i 6 mesi', 'più di 6 mesi'])
        self.grid_layout.addWidget(self.mesi, 13, 1, 1, 2)

        btn = QPushButton("OK")
        btn.clicked.connect(self.check_anamnesi_completa)
        self.grid_layout.addWidget(btn, 14, 0, -1, 3)

        self.setLayout(self.grid_layout)
        self.setFont(QFont('Arial Nova Light', 10))
        self.setWindowTitle("Questionario anamnestico")
        self.setWindowIcon(QIcon('appuntamentovaccino/data/CovidFree_Clinica.png'))

        self.setMaximumSize(700, 400)
        self.resize(700, 400)
        self.move(630, 100)

    def get_domanda(self, chiave, domanda, riga):
        label = QLabel(domanda)

        btn1 = QRadioButton('Sì')
        btn2 = QRadioButton('No')
        bg = QButtonGroup(self)
        bg.addButton(btn1)
        bg.addButton(btn2)

        self.grid_layout.addWidget(label, riga, 0)
        self.grid_layout.addWidget(btn1, riga, 1)
        self.grid_layout.addWidget(btn2, riga, 2)
        self.info[chiave] = bg

    # Funzione che controlla se l'anamnesi è stata completata correttamente.
    def check_anamnesi_completa(self):
        controllo = True

        for key in self.info.keys():
            if self.info[key].checkedButton() is None and controllo is True:
                controllo = False
            if self.mesi.currentText() == ' ':
                controllo = False

        if controllo:
            self.anamnesi['Pfizer'] = self.info['Pfizer'].checkedButton().text()
            self.anamnesi['Moderna'] = self.info['Moderna'].checkedButton().text()
            self.anamnesi['Astrazeneca'] = self.info['Astrazeneca'].checkedButton().text()
            self.anamnesi['Reazione grave'] = self.info['Reazione grave'].checkedButton().text()
            self.anamnesi['Malattie'] = self.info['Malattie'].checkedButton().text()
            self.anamnesi['Sistema immunitario'] = self.info['Sistema immunitario'].checkedButton().text()
            self.anamnesi['Gravidanza'] = self.info['Gravidanza'].checkedButton().text()
            self.anamnesi['Contatto'] = self.info['Contatto'].checkedButton().text()
            self.anamnesi['Sintomi'] = self.info['Sintomi'].checkedButton().text()
            self.anamnesi['Positivo COVID-19'] = self.mesi.currentText()
            self.close()
        else:
            QMessageBox.critical(self, 'Errore', 'Per favore, rispondi a tutte le domande', QMessageBox.Ok, QMessageBox.Ok)