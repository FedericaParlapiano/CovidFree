from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QGridLayout, \
    QDesktopWidget
from appuntamentovaccino.controller.ControlloreAppuntamentoVaccino import ControlloreAppuntamentoVaccino

class VistaAppuntamentoVaccino(QWidget):

    def __init__(self, appuntamento, parent=None):
        super(VistaAppuntamentoVaccino, self).__init__(parent)
        self.controller = ControlloreAppuntamentoVaccino(appuntamento)

        self.grid_layout = QGridLayout()
        v_layout = QVBoxLayout()

        font = QFont('Arial Nova Light')

        label_data = QLabel("Data: {} ".format(self.controller.get_data_appuntamento()))
        font.setPointSize(19)
        font.setCapitalization(True)
        label_data.setFont(font)
        label_data.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label_data)

        label_ora = QLabel("Orario: {} ".format(self.controller.get_orario_appuntamento()))
        label_ora.setFont(font)
        label_ora.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label_ora)

        v_layout.addItem(QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_tipo = QLabel("Tipo vaccino: {}".format(self.controller.get_vaccino_appuntamento()))
        font.setPointSize(15)
        label_tipo.setFont(font)
        label_tipo.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label_tipo)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        pixmap = QPixmap('appuntamentovaccino/data/{}.png'.format(self.controller.get_vaccino_appuntamento()))
        pixmap5 = pixmap.scaled(100, 30)
        pixmap.size()
        label_im = QLabel()
        label_im.setPixmap(pixmap5)
        label_im.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label_im)

        label_id = QLabel("{}".format(self.controller.get_id_appuntamento()))
        label_id.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label_id)
        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_nome = QLabel("Nome e cognome: {} {}".format(self.controller.get_cartella_paziente_appuntamento().nome, self.controller.get_cartella_paziente_appuntamento().cognome))
        font.setPointSize(18)
        font.setItalic(True)
        label_nome.setFont(font)
        v_layout.addWidget(label_nome)
        font.setItalic(False)

        label = QLabel("Dati personali")
        font.setPointSize(15)
        font.setUnderline(True)
        label.setFont(font)
        v_layout.addWidget(label)
        font.setUnderline(False)

        label_cf = QLabel("Codice fiscale: {}".format(self.controller.get_cartella_paziente_appuntamento().cf))
        font.setPointSize(12)
        label_cf.setFont(font)
        v_layout.addWidget(label_cf)

        label_telefono = QLabel("Telefono: {}".format(self.controller.get_cartella_paziente_appuntamento().telefono))
        label_telefono.setFont(font)
        v_layout.addWidget(label_telefono)

        label_indirizzo = QLabel("Indirizzo: {}".format(self.controller.get_cartella_paziente_appuntamento().indirizzo))
        label_indirizzo.setFont(font)
        v_layout.addWidget(label_indirizzo)

        label_data_nascita = QLabel("Data di nascita: {}".format(self.controller.get_cartella_paziente_appuntamento().data_di_nascita))
        label_data_nascita.setFont(font)
        v_layout.addWidget(label_data_nascita)

        label_categoria = QLabel("Categoria: {}".format(self.controller.get_cartella_paziente_appuntamento().categoria))
        label_categoria.setFont(font)
        v_layout.addWidget(label_categoria)

        if appuntamento.is_a_domicilio:
            label_is_a_domicilio = QLabel("Appuntamento a domicilio: Richiesto")
        else:
            label_is_a_domicilio = QLabel("Appuntamento a domicilio: Non richiesto")
        label_is_a_domicilio.setFont(font)
        v_layout.addWidget(label_is_a_domicilio)
        v_layout.addItem(QSpacerItem(30, 50, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_anamnesi = QLabel("Anamnesi")
        font.setPointSize(14)
        font.setUnderline(True)
        label_anamnesi.setFont(font)
        v_layout.addWidget(label_anamnesi)

        self.get_label_anamnesi("Soffre di allergie ad uno dei componenti del vaccino Astrazeneca?", "Astrazeneca", 0)
        self.get_label_anamnesi("Soffre di allergie ad uno dei componenti del vaccino Moderna?", "Moderna", 1)
        self.get_label_anamnesi("Soffre di allergie ad uno dei componenti del vaccino Pfizer?", "Pfizer", 2)
        self.get_label_anamnesi("Ha mai avuto una reazione grave dopo aver ricevuto un vaccino?", "Reazione grave", 3)
        self.get_label_anamnesi("Soffre di malattie cardiache o polmonari, asma, malattie renali, diabete, anemia o altre malattie del sangue?", "Malattie", 4)
        self.get_label_anamnesi("Si trova in una condizione di compromissione del sistema immunitario (esempio: cancro, leucemia, linfoma, HIV/AIDS, trapianto)?", "Sistema immunitario", 5)
        self.get_label_anamnesi("È incinta o sta pensando di rimanere incinta nel prossimo mese?", "Gravidanza", 6)
        self.get_label_anamnesi("Nell\'ultimo mese è stato in contatto con una persona contagiata da Sars-CoV2 o affetta da COVID-19?", "Contatto", 7)
        self.get_label_anamnesi("Manifesta sintomi riconducibili a infezione da COVID-19?", "Sintomi", 8)
        self.get_label_anamnesi("Se è stato precedentemente affetto da COVID-19, indicare quanti mesi sono trascorsi dall\'infezione:", "Positivo COVID-19", 9)

        v_layout.addLayout(self.grid_layout)
        self.setLayout(v_layout)
        self.setFont(QFont('Arial Nova Light', 14))
        self.setWindowTitle("Appuntamento Vaccino " + self.controller.get_cartella_paziente_appuntamento().nome + " " + self.controller.get_cartella_paziente_appuntamento().cognome)
        self.setWindowIcon(QIcon('appuntamentovaccino/data/CovidFree_Clinica.png'))

        self.setMaximumSize(800, 700)
        self.resize(800, 700)
        self.move(0, 0)

    # Funzione che viene richiamata per la scrittura delle domande dell'anamnesi.
    def get_label_anamnesi(self, domanda, chiave, posizione):
        label_domanda = QLabel(domanda + " " + self.controller.get_cartella_paziente_appuntamento().anamnesi[chiave])
        font_domanda = label_domanda.font()
        font_domanda.setPointSize(12)
        label_domanda.setFont(font_domanda)
        self.grid_layout.addWidget(label_domanda, posizione, 0)