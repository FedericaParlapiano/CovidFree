from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from appuntamentovaccino.controller.ControlloreAppuntamentoVaccino import ControlloreAppuntamentoVaccino


class VistaAppuntamentoVaccino(QWidget):

    def __init__(self, appuntamento, parent=None):
        super(VistaAppuntamentoVaccino, self).__init__()
        #self.controller = ControlloreAppuntamentoVaccino(appuntamento)

        v_layout = QVBoxLayout()

        print("sono dentro")

        label_nome = QLabel("Paziente: {} {}".format(appuntamento.cartella_paziente.nome, appuntamento.cartella_paziente.cognome))
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        print("ci provo")

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_data = QLabel("Data e ora: {} {}".format(appuntamento.data_appuntamento, appuntamento.fascia_oraria))
        font_data = label_data.font()
        font_data.setPointSize(20)
        label_data.setFont(font_data)
        v_layout.addWidget(label_data)

        print("ci sto provando")

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(v_layout)

        print("non capisco")

        self.setWindowTitle("Appuntamento Vaccino")

        print("per scrupolo")
