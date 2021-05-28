from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel

from materiale.controller.ControlloreMateriale import ControlloreMateriale

class VistaTampone(QWidget):
    def __init__(self, tampone, parent=None):
        super(VistaTampone, self).__init__(parent)
        self.controller = ControlloreMateriale(tampone)

        v_layout = QGridLayout()

        label_nome = QLabel("Tampone: {}".format(self.controller.get_tipologia_materiale()))
        font_nome = label_nome.font()
        font_nome.setPointSize(36)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        label_id = QLabel("Id: {}".format(self.controller.get_id_materiale()))
        font_id = label_id.font()
        font_id.setPointSize(16)
        label_id.setFont(font_id)
        v_layout.addWidget(label_id)

        label_quantita = QLabel("Quantità: {}".format(self.controller.get_quantita_materiale()))
        font_quantita = label_quantita.font()
        font_quantita.setPointSize(16)
        label_quantita.setFont(font_quantita)
        v_layout.addWidget(label_quantita)

        label_prezzo = QLabel("Prezzo: {}".format(self.controller.get_prezzo_tampone))
        font_prezzo = label_prezzo.font()
        font_prezzo.setPointSize(16)
        label_prezzo.setFont(font_prezzo)
        v_layout.addWidget(label_prezzo)

        self.setLayout(v_layout)








