from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel

from materiale.controller.ControlloreMateriale import ControlloreMateriale

class VistaVaccino(QWidget):
    def __init__(self, vaccino, parent=None):
        super(VistaVaccino, self).__init__(parent)
        self.controller = ControlloreMateriale(vaccino)

        v_layout = QGridLayout()

        label_nome = QLabel("Vaccino: {}".format(self.controller.get_tipologia_materiale()))
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

        if self.controller.get_is_doppia_dose_vaccino:
            label_monodose = QLabel("Dosi previste: 2")
        else:
            label_monodose = QLabel("Dosi previste: 1")
        font_monodose = label_id.font()
        font_monodose.setPointSize(16)
        label_monodose.setFont(font_monodose)
        v_layout.addWidget(label_monodose)

        label_distanza = QLabel("Distanza: {}".format(self.controller.get_distanza_seconda_dose_vaccino()))
        font_distanza = label_distanza.font()
        font_distanza.setPointSize(16)
        label_distanza.setFont(font_quantita)
        v_layout.addWidget(label_distanza)

        self.setLayout(v_layout)