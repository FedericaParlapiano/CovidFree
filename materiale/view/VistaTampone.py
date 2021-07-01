from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt

from materiale.controller.ControlloreMateriale import ControlloreMateriale

class VistaTampone(QWidget):
    def __init__(self, tampone, parent=None):
        super(VistaTampone, self).__init__(parent)

        self.controller = ControlloreMateriale(tampone)
        v_layout = QVBoxLayout()
        font = QFont('Arial Nova Light')

        label = QLabel("Tampone")

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

        label_prezzo = QLabel("Prezzo: €{}".format(self.controller.get_prezzo_tampone()))
        label_prezzo.setFont(font)
        v_layout.addWidget(label_prezzo)

        self.setWindowTitle("Tampone " + self.controller.get_tipologia_materiale())
        self.setFont(QFont('Arial Nova Light'))
        self.setWindowIcon(QIcon('appuntamentovaccino/data/CovidFree_Clinica.png'))
        self.setLayout(v_layout)

        self.setMaximumSize(400, 300)
        self.resize(400, 300)
        self.move(300, 200)








