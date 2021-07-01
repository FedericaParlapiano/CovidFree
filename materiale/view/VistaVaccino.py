from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt
from materiale.controller.ControlloreMateriale import ControlloreMateriale

class VistaVaccino(QWidget):
    def __init__(self, vaccino, parent=None):
        super(VistaVaccino, self).__init__(parent)
        self.controller = ControlloreMateriale(vaccino)

        v_layout = QVBoxLayout()
        font = QFont('Arial Nova Light')

        label = QLabel("Vaccino")
        label.setStyleSheet("border-radius: 20px; border: 2px solid black;")
        font.setPointSize(25)
        font.setCapitalization(True)
        label.setFont(font)
        label.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label)
        font.setCapitalization(False)

        label_nome = QLabel("Tipo: \'{}\'".format(self.controller.get_tipologia_materiale()))
        font.setPointSize(20)
        label_nome.setFont(font)
        v_layout.addWidget(label_nome)

        line = QSpacerItem(0, 30, QSizePolicy.Minimum, QSizePolicy.Minimum)
        v_layout.addItem(line)

        label_id = QLabel("Id: {}".format(self.controller.get_id_materiale()))
        font.setPointSize(16)
        font.setItalic(True)
        label_id.setFont(font)
        v_layout.addWidget(label_id)

        label_quantita = QLabel("Quantità: {}".format(self.controller.get_quantita_materiale()))
        label_quantita.setFont(font)
        v_layout.addWidget(label_quantita)

        if self.controller.get_is_doppia_dose_vaccino:
            label_monodose = QLabel("Dosi previste: 2")
        else:
            label_monodose = QLabel("Dosi previste: 1")
        label_monodose.setFont(font)
        v_layout.addWidget(label_monodose)

        label_distanza = QLabel("Giorni di distanza tra le due dosi: {}".format(self.controller.get_distanza_seconda_dose_vaccino()))
        label_distanza.setFont(font)
        v_layout.addWidget(label_distanza)

        self.setWindowTitle("Vaccino " + self.controller.get_tipologia_materiale())
        self.setWindowIcon(QIcon('appuntamentovaccino/data/CovidFree_Clinica.png'))
        self.setFont(QFont('Arial Nova Light'))
        self.setLayout(v_layout)

        self.setMaximumSize(400, 300)
        self.resize(400, 300)
        self.move(250, 190)

