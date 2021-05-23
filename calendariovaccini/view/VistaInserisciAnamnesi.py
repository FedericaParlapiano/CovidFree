from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QRadioButton, QButtonGroup, QPushButton, QSpacerItem, \
    QSizePolicy


class VistaInserisciAnamnesi(QWidget):

    def __init__(self, controller, callback):

        super(VistaInserisciAnamnesi, self).__init__(parent=None)
        self.controller = controller
        self.callback = callback
        self.info = {}

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(QLabel('Da compilare a cura del personale e da riesaminare insieme ai Professionisti Sanitari addetti alla vaccinazione.'), 1, 0)
        self.grid_layout.addWidget(QLabel(' '))

        self.grid_layout.addWidget(QLabel('Soffre di allergie ad uno dei componenti del vaccino ?'), 2, 0)
        self.get_domanda('Pfizer', 3)
        self.get_domanda('Moderna', 4)
        self.get_domanda('Astrazenca', 5)
        self.get_domanda('Ha mai avuto una reazione grave dopo aver ricevuto un vaccino?', 6)
        self.get_domanda('Soffre di malattie cardiache o polmonari, asma, malattie renali, diabete, anemia o altre malattie del sangue?', 7)
        self.get_domanda('Si trova in una condizione di compromissione del sistema immunitario (esempio: cancro, leucemia, linfoma, HIV/AIDS, trapianto)?', 8)
        self.get_domanda('È incinta o sta pensando di rimanere incinta nel prossimo mese?', 9)

        self.grid_layout.addWidget(QLabel(' '))
        self.grid_layout.addWidget(QLabel('Anamnesi COVID-Correlata'), 10, 0)
        self.get_domanda(' Nell\'ultimo mese è stato in contatto con una persona contagiata da Sars-CoV2 o affetta da COVID-19?', 11)
        self.get_domanda('Manifesta sistomi riconducibili a infezione da COVID-19?', 12)

        btn = QPushButton("OK")
        btn.clicked.connect(self.check_anamnesi_completa)
        self.grid_layout.addWidget(btn)

        self.setLayout(self.grid_layout)

    def get_domanda(self, domanda, riga):

        label = QLabel(domanda)

        btn1 = QRadioButton('Sì')
        btn2 = QRadioButton('No')
        bg = QButtonGroup(self)

        btn1.toggled.connect(self.onClicked)
        btn2.toggled.connect(self.onClicked)
        bg.addButton(btn1)
        bg.addButton(btn2)

        self.grid_layout.addWidget(label, riga, 0)
        self.grid_layout.addWidget(btn1, riga, 1)
        self.grid_layout.addWidget(btn2, riga, 2)


    def onClicked(self):
        pass

    def check_anamnesi_completa(self):

        pass



