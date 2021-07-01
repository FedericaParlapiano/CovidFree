from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QDesktopWidget

from appuntamentotampone.controller.ControlloreAppuntamentoTampone import ControlloreAppuntamentoTampone


class VistaAppuntamentoTampone(QWidget):

    def __init__(self, appuntamento, parent=None):
        super(VistaAppuntamentoTampone, self).__init__()
        self.controller = ControlloreAppuntamentoTampone(appuntamento)

        v_layout = QVBoxLayout()

        label_data = QLabel("Data: {} ".format(self.controller.get_data_appuntamento()))
        font_data = label_data.font()
        font_data.setPointSize(20)
        font_data.setFamily('Georgia')
        font_data.setCapitalization(True)
        label_data.setFont(font_data)
        label_data.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label_data)

        label_ora = QLabel("Orario: {} ".format(self.controller.get_fascia_oraria()))
        font_ora = label_ora.font()
        font_ora.setPointSize(20)
        font_ora.setFamily('Georgia')
        label_ora.setFont(font_data)
        label_ora.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label_ora)

        v_layout.addItem(QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_tipo = QLabel("Tipo tampone: {}".format(self.controller.get_tipo_tampone()))
        font_tipo = label_tipo.font()
        font_tipo.setPointSize(18)
        font_tipo.setFamily('Georgia')
        label_tipo.setFont(font_tipo)
        label_tipo.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label_tipo)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_nome = QLabel("Nome e cognome: {} {}".format(self.controller.get_nome(), self.controller.get_cognome()))
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

        label_cf = QLabel("Codice fiscale: {}".format(self.controller.get_cf()))
        font_cf = label_cf.font()
        font_cf.setPointSize(12)
        font_cf.setFamily('Georgia')
        label_cf.setFont(font_cf)
        v_layout.addWidget(label_cf)

        label_telefono = QLabel("Telefono: {}".format(self.controller.get_telefono()))
        font_telefono = label_telefono.font()
        font_telefono.setPointSize(12)
        font_telefono.setFamily('Georgia')
        label_telefono.setFont(font_telefono)
        v_layout.addWidget(label_telefono)

        label_indirizzo = QLabel("Indirizzo: {}".format(self.controller.get_indirizzo()))
        font_indirizzo = label_indirizzo.font()
        font_indirizzo.setPointSize(12)
        font_indirizzo.setFamily('Georgia')
        label_indirizzo.setFont(font_indirizzo)
        v_layout.addWidget(label_indirizzo)

        label_data_nascita = QLabel("Data di nascita: {}".format(self.controller.get_data_nascita()))
        font_data_nascita = label_data_nascita.font()
        font_data_nascita.setPointSize(12)
        font_data_nascita.setFamily('Georgia')
        label_data_nascita.setFont(font_data_nascita)
        v_layout.addWidget(label_data_nascita)

        if self.controller.get_is_drive_through():
            label_drive_through = QLabel("Drive Through: Prenotato")
        else:
            label_drive_through = QLabel("Drive Through: Non Richiesto")
        font_drive_through = label_drive_through.font()
        font_drive_through.setPointSize(12)
        font_drive_through.setFamily('Georgia')
        label_drive_through.setFont(font_drive_through)
        v_layout.addWidget(label_drive_through)

        self.setLayout(v_layout)
        self.setWindowTitle("Appuntamento Tampone " + self.controller.get_nome() + " " + self.controller.get_cognome())
        self.setWindowIcon(QIcon('appuntamentovaccino/data/CovidFree_Clinica.png'))

        self.setMaximumSize(400, 500)
        self.resize(400, 500)
        self.move(200, 100)
