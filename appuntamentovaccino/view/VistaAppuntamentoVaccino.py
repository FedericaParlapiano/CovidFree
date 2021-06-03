from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from appuntamentovaccino.controller.ControlloreAppuntamentoVaccino import ControlloreAppuntamentoVaccino


class VistaAppuntamentoVaccino(QWidget):

    def __init__(self, appuntamento, callback_eliminazione, elimina_appuntamento, parent=None):
        super(VistaAppuntamentoVaccino, self).__init__()
        self.controller = ControlloreAppuntamentoVaccino(appuntamento)
        self.elimina_appuntamento = elimina_appuntamento
        self.callback_eliminazione = callback_eliminazione

        v_layout = QVBoxLayout()

        label_nome = QLabel("Paziente: {} {}".format(self.controller.self.controller.get_cartella_paziente_appuntamento().nome,
                                                       self.controller.self.controller.get_cartella_paziente_appuntamento().cognome))
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_data = QLabel("Data e ora: {} {}".format(self.controller.get_data_appuntamento(), self.controller.get_orario_appuntamento()))
        font_data = label_data.font()
        font_data.setPointSize(20)
        label_data.setFont(font_data)
        v_layout.addWidget(label_data)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_appuntamento_click)
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle("Appuntamento Vaccino")

    def elimina_appuntamento_click(self):
        self.elimina_appuntamento(self.controller.get_id_appuntamento())
        self.elimina_callback()
        self.close()