from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QRadioButton, QButtonGroup


class VistaInserisciAnamnesi(QWidget):

    def __init__(self, controller, callback):

        super(VistaInserisciAnamnesi, self).__init__(parent=None)
        self.controller = controller
        self.callback = callback
        self.info = {}

        self.grid_layout = QGridLayout()
        self.nota1 = QLabel('Da compilare a cura del personale e da riesaminare insieme ai Professionisti Sanitari addetti alla vaccinazione.')
        self.grid_layout.addWidget(self.nota1)
        self.spazio = QLabel(' ')
        self.grid_layout.addWidget(self.spazio)

        self.get_domanda('Attualmente è malato?', 1)
        self.get_domanda('Ha febbre?', 2)
        self.get_domanda('Soffre di allergie al lattice, a qualche cibo, a farmaci o ai componenti del vaccino?', 3)
        self.get_domanda('Ha mai avuto una reazione grave dopo aver ricevuto un vaccino?', 4)
        self.get_domanda('Soffre di malattie cardiache o polmonari, asma, malattie renali, diabete, anemia o altre malattie del sangue?', 5)
        self.get_domanda('Si trova in una condizione di compromissione del sistema immunitario (esempio: cancro, leucemia, linfoma, HIV/AIDS, trapianto)?', 6)
        self.get_domanda('Negli ultimi 3 mesi ha assunto farmaci che indeboliscono il sistema immunitario (esmepio: cortisone, prednisone o altri steroidi) o farmaci antitumorali, oppure ha subito trattamenti con radiazioni?', 7)
        self.get_domanda('Durante lo scorso anno, ha ricevuto una trasfusione di sanque o prodotti ematici, oppure le sono stati somministrati immunoglobuline o farmaci antivirali', 8)
        self.get_domanda('Ha avuto attacchi di convulsioni o qualche problema al cervello o al sistema nervoso?', 9)
        self.get_domanda('Ha ricevuto vaccinazioni nelle ultime 4 settimane?', 10)

        self.nota2 = QLabel('Per le donne:')
        self.grid_layout.addWidget(self.nota2, 11, 0)
        self.get_domanda('è incinta o sta pensando di rimanere incinta nel prossimo mese?', 12)
        self.get_domanda('Sta allattando?', 13)

        self.nota3 = QLabel('Anamnesi COVID-Correlata')
        self.grid_layout.addWidget(self.nota3, 14, 0)
        self.get_domanda(' Nell\'ultimo mese è stato in contatto con una persona contagiata da Sars-CoV2 o affetta da COVID-19?', 15)
        self.get_domanda('Manifesta sistomi riconducibili a infezione da COVID-19?', 16)
        self.get_domanda('Ha fatto qualche viaggio internazionale nell\'ultimo mese?', 17)
        self.get_domanda('Test covid: ???????', 18)

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




