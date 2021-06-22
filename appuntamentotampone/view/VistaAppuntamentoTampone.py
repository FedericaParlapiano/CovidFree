from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from appuntamentotampone.controller.ControlloreAppuntamentoTampone import ControlloreAppuntamentoTampone


class VistaAppuntamentoTampone(QWidget):

    def __init__(self, appuntamento, parent=None):
        super(VistaAppuntamentoTampone, self).__init__()
        self.controller = ControlloreAppuntamentoTampone(appuntamento)
        #self.elimina_appuntamento = elimina_appuntamento
        #self.callback_eliminazione = callback_eliminazione

        v_layout = QVBoxLayout()

        label_nome = QLabel("Nome e cognome: {} {}".format(self.controller.get_nome(), self.controller.get_cognome()))
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_data = QLabel("Data e fascia oraria: {} {}".format(self.controller.get_data_appuntamento(), self.controller.get_fascia_oraria()))
        font_data = label_data.font()
        font_data.setPointSize(20)
        label_data.setFont(font_data)
        v_layout.addWidget(label_data)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_cf = QLabel("Codice fiscale: {}".format(self.controller.get_cf()))
        font_cf = label_cf.font()
        font_cf.setPointSize(20)
        label_cf.setFont(font_cf)
        v_layout.addWidget(label_cf)

        label_telefono = QLabel("Telefono: {}".format(self.controller.get_telefono()))
        font_telefono = label_telefono.font()
        font_telefono.setPointSize(20)
        label_telefono.setFont(font_telefono)
        v_layout.addWidget(label_telefono)

        label_indirizzo = QLabel("Indirizzo: {}".format(self.controller.get_indirizzo()))
        font_indirizzo = label_indirizzo.font()
        font_indirizzo.setPointSize(20)
        label_indirizzo.setFont(font_indirizzo)
        v_layout.addWidget(label_indirizzo)

        label_data_nascita = QLabel("Data di nascita: {}".format(self.controller.get_data_nascita()))
        font_data_nascita = label_data_nascita.font()
        font_data_nascita.setPointSize(20)
        label_data_nascita.setFont(font_data_nascita)
        v_layout.addWidget(label_data_nascita)

        label_drive_through = QLabel("Drive Through: {}".format(self.controller.get_is_drive_through()))
        font_drive_through = label_drive_through.font()
        font_drive_through.setPointSize(20)
        label_drive_through.setFont(font_drive_through)
        v_layout.addWidget(label_drive_through)

        label_tipo = QLabel("Tipo tampone: {}".format(self.controller.get_tipo_tampone()))
        font_tipo = label_tipo.font()
        font_tipo.setPointSize(20)
        label_tipo.setFont(font_tipo)
        v_layout.addWidget(label_tipo)

        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_appuntamento_click)
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle("Appuntamento Tampone")

    def elimina_appuntamento_click(self):
        pass