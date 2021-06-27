from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QGridLayout

from appuntamentovaccino.controller.ControlloreAppuntamentoVaccino import ControlloreAppuntamentoVaccino


class VistaAppuntamentoVaccino(QWidget):

    def __init__(self, appuntamento, parent=None):
        super(VistaAppuntamentoVaccino, self).__init__()
        self.controller = ControlloreAppuntamentoVaccino(appuntamento)
        self.grid_layout = QGridLayout()

        v_layout = QVBoxLayout()

        label_data = QLabel("Data: {} ".format(self.controller.get_data_appuntamento()))
        font_data = label_data.font()
        font_data.setPointSize(20)
        font_data.setFamily('Georgia')
        font_data.setCapitalization(True)
        label_data.setFont(font_data)
        label_data.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label_data)

        label_ora = QLabel("Orario: {} ".format(self.controller.get_orario_appuntamento()))
        font_ora = label_ora.font()
        font_ora.setPointSize(20)
        font_ora.setFamily('Georgia')
        label_ora.setFont(font_data)
        label_ora.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label_ora)

        v_layout.addItem(QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_tipo = QLabel("Tipo vaccino: {}".format(self.controller.get_vaccino_appuntamento()))
        font_tipo = label_tipo.font()
        font_tipo.setPointSize(18)
        font_tipo.setFamily('Georgia')
        label_tipo.setFont(font_tipo)
        label_tipo.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label_tipo)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_id = QLabel("{}".format(self.controller.get_id_appuntamento()))
        font_id = label_id.font()
        font_id.setPointSize(15)
        font_id.setFamily('Georgia')
        label_id.setFont(font_id)
        label_id.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label_id)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_nome = QLabel("Nome e cognome: {} {}".format(self.controller.get_cartella_paziente_appuntamento().nome, self.controller.get_cartella_paziente_appuntamento().cognome))
        font_nome = label_nome.font()
        font_nome.setPointSize(20)
        font_nome.setFamily('Georgia')
        font_nome.setItalic(True)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        label = QLabel("Dati personali")
        font = label.font()
        font.setPointSize(15)
        font.setFamily('Georgia')
        font.setUnderline(True)
        label.setFont(font)
        v_layout.addWidget(label)

        label_cf = QLabel("Codice fiscale: {}".format(self.controller.get_cartella_paziente_appuntamento().cf))
        font_cf = label_cf.font()
        font_cf.setPointSize(12)
        font_cf.setFamily('Georgia')
        label_cf.setFont(font_cf)
        v_layout.addWidget(label_cf)

        label_telefono = QLabel("Telefono: {}".format(self.controller.get_cartella_paziente_appuntamento().telefono))
        font_telefono = label_telefono.font()
        font_telefono.setPointSize(12)
        font_telefono.setFamily('Georgia')
        label_telefono.setFont(font_telefono)
        v_layout.addWidget(label_telefono)

        label_indirizzo = QLabel("Indirizzo: {}".format(self.controller.get_cartella_paziente_appuntamento().indirizzo))
        font_indirizzo = label_indirizzo.font()
        font_indirizzo.setPointSize(12)
        font_indirizzo.setFamily('Georgia')
        label_indirizzo.setFont(font_indirizzo)
        v_layout.addWidget(label_indirizzo)

        label_data_nascita = QLabel("Data di nascita: {}".format(self.controller.get_cartella_paziente_appuntamento().data_di_nascita))
        font_data_nascita = label_data_nascita.font()
        font_data_nascita.setPointSize(12)
        font_data_nascita.setFamily('Georgia')
        label_data_nascita.setFont(font_data_nascita)
        v_layout.addWidget(label_data_nascita)

        if appuntamento.is_a_domicilio:
            label_is_a_domicilio = QLabel("Appuntamento a domicilio: Richiesto")
        else:
            label_is_a_domicilio = QLabel("Appuntamento a domicilio: Non richiesto")
        font_is_a_domicilio = label_is_a_domicilio.font()
        font_is_a_domicilio.setPointSize(12)
        font_is_a_domicilio.setFamily('Georgia')
        label_is_a_domicilio.setFont(font_is_a_domicilio)
        v_layout.addWidget(label_is_a_domicilio)

        v_layout.addItem(QSpacerItem(30, 50, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_anamnesi = QLabel("Anamnesi")
        font_anamnesi = label_anamnesi.font()
        font_anamnesi.setPointSize(15)
        font_anamnesi.setFamily('Georgia')
        font_anamnesi.setUnderline(True)
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

        self.setWindowTitle("Appuntamento Vaccino " + self.controller.get_cartella_paziente_appuntamento().nome + " " + self.controller.get_cartella_paziente_appuntamento().cognome)


    def get_label_anamnesi(self, domanda, chiave, posizione):
        label_domanda = QLabel(domanda + " " + self.controller.get_cartella_paziente_appuntamento().anamnesi[chiave])
        font_domanda = label_domanda.font()
        font_domanda.setPointSize(12)
        font_domanda.setFamily('Georgia')
        label_domanda.setFont(font_domanda)
        self.grid_layout.addWidget(label_domanda, posizione, 0)




