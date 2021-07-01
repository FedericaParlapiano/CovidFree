from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QDesktopWidget

from appuntamentotampone.controller.ControlloreAppuntamentoTampone import ControlloreAppuntamentoTampone


class VistaAppuntamentoTampone(QWidget):

    def __init__(self, appuntamento, parent=None):
        super(VistaAppuntamentoTampone, self).__init__(parent)
        self.controller = ControlloreAppuntamentoTampone(appuntamento)

        v_layout = QVBoxLayout()

        font = QFont('Arial Nova Light')

        label_data = QLabel("Data: {} ".format(self.controller.get_data_appuntamento()))
        font.setPointSize(18)
        font.setCapitalization(True)
        label_data.setFont(font)
        label_data.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label_data)
        font.setCapitalization(False)

        label_ora = QLabel("Orario: {} ".format(self.controller.get_fascia_oraria()))
        font_ora = label_ora.font()
        label_ora.setFont(font)
        label_ora.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label_ora)

        v_layout.addItem(QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_tipo = QLabel("Tipo tampone: {}".format(self.controller.get_tipo_tampone()))
        font_tipo = label_tipo.font()
        font_tipo.setPointSize(19)
        label_tipo.setFont(font_tipo)
        label_tipo.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label_tipo)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_nome = QLabel("Nome e cognome: {} {}".format(self.controller.get_nome(), self.controller.get_cognome()))
        font.setPointSize(20)
        font.setItalic(True)
        label_nome.setFont(font)
        v_layout.addWidget(label_nome)
        font.setItalic(False)

        label = QLabel("Dati personali")
        font.setPointSize(14)
        font.setUnderline(True)
        label.setFont(font)
        v_layout.addWidget(label)
        font.setUnderline(False)

        label_cf = QLabel("Codice fiscale: {}".format(self.controller.get_cf()))
        font.setPointSize(12)
        label_cf.setFont(font)
        v_layout.addWidget(label_cf)

        label_telefono = QLabel("Telefono: {}".format(self.controller.get_telefono()))
        label_telefono.setFont(font)
        v_layout.addWidget(label_telefono)

        label_indirizzo = QLabel("Indirizzo: {}".format(self.controller.get_indirizzo()))
        label_indirizzo.setFont(font)
        v_layout.addWidget(label_indirizzo)

        label_data_nascita = QLabel("Data di nascita: {}".format(self.controller.get_data_nascita()))
        label_data_nascita.setFont(font)
        v_layout.addWidget(label_data_nascita)

        if self.controller.get_is_drive_through():
            label_drive_through = QLabel("Drive Through: Prenotato")
        else:
            label_drive_through = QLabel("Drive Through: Non Richiesto")
        label_drive_through.setFont(font)
        v_layout.addWidget(label_drive_through)

        self.setLayout(v_layout)
        self.setFont(QFont('Arial Nova Light', 14))
        self.setWindowTitle("Appuntamento Tampone " + self.controller.get_nome() + " " + self.controller.get_cognome())
        self.setWindowIcon(QIcon('appuntamentovaccino/data/CovidFree_Clinica.png'))

        self.setMaximumSize(400, 500)
        self.resize(400, 500)
        self.move(200, 100)