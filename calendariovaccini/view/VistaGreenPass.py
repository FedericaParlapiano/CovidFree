from datetime import timedelta, datetime

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QSpacerItem, QSizePolicy, QHBoxLayout, QMessageBox, \
    QPushButton

from calendariovaccini.controller.ControlloreCalendarioVaccini import ControlloreCalendarioVaccini


class VistaGreenPass(QWidget):

    def __init__(self, appuntamento, parent = None):
        super(VistaGreenPass, self).__init__(parent)
        self.controller = ControlloreCalendarioVaccini()

        self.appuntamento = appuntamento

        v_layout = QVBoxLayout()
        v_layout_l =QVBoxLayout()
        h_layout = QHBoxLayout()

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        pixmap = QPixmap('appuntamentovaccino/data/qrcode.png')
        pixmap5 = pixmap.scaled(300, 300)
        pixmap.size()
        label_im = QLabel()
        label_im.setPixmap(pixmap5)
        label_im.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label_im)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_nome1 = QLabel("Cognome e Nome")
        v_layout.addWidget(label_nome1)

        label_nome2 = QLabel("Surname(s) and forename(s)".format(appuntamento.cartella_paziente.nome, appuntamento.cartella_paziente.cognome))
        font_nome2 = label_nome2.font()
        font_nome2.setPointSize(10)
        label_nome2.setFont(font_nome2)
        v_layout.addWidget(label_nome2)

        label_nome3 = QLabel(appuntamento.cartella_paziente.cognome + " " + appuntamento.cartella_paziente.nome)
        font_nome3 = label_nome3.font()
        font_nome3.setPointSize(18)
        font_nome3.setCapitalization(True)
        label_nome3.setFont(font_nome3)
        v_layout.addWidget(label_nome3)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_data_nascita1 = QLabel("Data di nascita")
        v_layout.addWidget(label_data_nascita1)

        label_data_nascita2 = QLabel("Date of birth(yyyy-mm-dd)")
        font_data_nascita2 = label_data_nascita2.font()
        font_data_nascita2.setPointSize(10)
        label_data_nascita2.setFont(font_data_nascita2)
        v_layout.addWidget(label_data_nascita2)

        data_nascita = datetime.strptime(appuntamento.data_appuntamento, '%d-%m-%Y')
        str_data_nascita = str(data_nascita.strftime('%Y-%m-%d'))

        label_data_nascita3 = QLabel(str_data_nascita)
        font_data_nascita3 = label_data_nascita3.font()
        font_data_nascita3.setPointSize(18)
        label_data_nascita3.setFont(font_data_nascita3)
        v_layout.addWidget(label_data_nascita3)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_cf1 = QLabel("Identificativo univoco del certificato")
        v_layout.addWidget(label_cf1)

        label_cf2 = QLabel("Unique Certificate Identifier")
        font_cf2 = label_cf2.font()
        font_cf2.setPointSize(10)
        label_cf2.setFont(font_cf2)
        v_layout.addWidget(label_cf2)

        label_cf3 = QLabel(appuntamento.cartella_paziente.cf)
        font_cf3 = label_cf3.font()
        font_cf3.setPointSize(18)
        label_cf3.setFont(font_cf3)
        v_layout.addWidget(label_cf3)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_data_scadenza = QLabel("Data di scadenza: {}".format(self.scadenza()))
        v_layout.addWidget(label_data_scadenza)

        label_europa = QLabel("Certificazione verde \n COVID-19 \n EU Digital \n COVID Certificate")
        font_europa = label_europa.font()
        font_europa.setPointSize(20)
        font_europa.setBold(True)
        font_europa.setItalic(True)
        label_europa.setFont(font_europa)
        label_europa.setAlignment(Qt.AlignCenter)
        v_layout_l.addWidget(label_europa)
        
        pixmap_eu = QPixmap('appuntamentovaccino/data/europa.png')
        pixmap2 = pixmap_eu.scaled(180, 120)
        label_eu = QLabel()
        label_eu.setPixmap(pixmap2)
        label_eu.setAlignment(Qt.AlignCenter)
        v_layout_l.addWidget(label_eu)

        h_layout.addLayout(v_layout)
        h_layout.addItem(QSpacerItem(50, 50, QSizePolicy.Minimum, QSizePolicy.Expanding))
        h_layout.addLayout(v_layout_l)

        btn = QPushButton("Invia")
        btn.clicked.connect(self.invio_green_pass)
        v_layout_l.addWidget(btn)

        self.setLayout(h_layout)
        self.setFont(QFont('Arial Nova Light', 15))
        self.setWindowTitle('Grenn pass {} {}' .format(appuntamento.cartella_paziente.nome, appuntamento.cartella_paziente.cognome))
        self.setWindowIcon(QIcon('appuntamentovaccino/data/CovidFree_Clinica.png'))

        self.setMaximumSize(500, 700)
        self.resize(500, 700)
        self.move(50, 0)

    def invio_green_pass(self):
        paziente = self.appuntamento.cartella_paziente.nome + ' ' + self.appuntamento.cartella_paziente.cognome
        telefono = self.appuntamento.cartella_paziente.telefono
        if telefono:
            QMessageBox.information(self, 'Invio Green Pass',
                                    "A breve il  Green Pass verrà inviato al numero " + telefono + " associato alla cartella del paziente " + paziente,
                                    QMessageBox.Ok, QMessageBox.Cancel)

    def scadenza(self):
        s = datetime.strptime(self.appuntamento.data_appuntamento, '%d-%m-%Y') + timedelta(days=270)
        scadenza = str(s.strftime('%d-%m-%Y'))
        return scadenza