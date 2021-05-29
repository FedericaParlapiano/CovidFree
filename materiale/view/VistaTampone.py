from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt

from materiale.controller.ControlloreMateriale import ControlloreMateriale

class VistaTampone(QWidget):
    def __init__(self, tampone, parent=None):
        super(VistaTampone, self).__init__(parent)
        self.controller = ControlloreMateriale(tampone)

        v_layout = QVBoxLayout()

        label = QLabel("Tampone")
        label.setStyleSheet("border-radius: 20px; border: 2px solid green;")
        font_label = label.font()
        font_label.setPointSize(30)
        font_label.setFamily('Georgia')
        font_label.setCapitalization(True)
        label.setFont(font_label)
        label.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label)

        label_nome = QLabel("Tipo: \'{}\'".format(self.controller.get_tipologia_materiale()))
        font_nome = label_nome.font()
        font_nome.setPointSize(20)
        font_nome.setFamily('Georgia')
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        line = QSpacerItem(0, 30, QSizePolicy.Minimum, QSizePolicy.Minimum)
        v_layout.addItem(line)

        label_id = QLabel("Id: {}".format(self.controller.get_id_materiale()))
        font_id = label_id.font()
        font_id.setPointSize(16)
        font_id.setFamily('Georgia')
        font_id.setItalic(True)
        label_id.setFont(font_id)
        v_layout.addWidget(label_id)

        label_quantita = QLabel("Quantità: {}".format(self.controller.get_quantita_materiale()))
        font_quantita = label_quantita.font()
        font_quantita.setPointSize(16)
        font_quantita.setFamily('Georgia')
        font_quantita.setItalic(True)
        label_quantita.setFont(font_quantita)
        v_layout.addWidget(label_quantita)

        label_prezzo = QLabel("Prezzo: €{}".format(self.controller.get_prezzo_tampone()))
        font_prezzo = label_prezzo.font()
        font_prezzo.setPointSize(16)
        font_prezzo.setFamily('Georgia')
        font_prezzo.setItalic(True)
        label_prezzo.setFont(font_prezzo)
        v_layout.addWidget(label_prezzo)

        self.setLayout(v_layout)
        self.adjustSize()








