from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt
from materiale.controller.ControlloreMateriale import ControlloreMateriale

class VistaVaccino(QWidget):
    def __init__(self, vaccino, parent=None):
        super(VistaVaccino, self).__init__(parent)
        self.controller = ControlloreMateriale(vaccino)

        v_layout = QVBoxLayout()

        label = QLabel("Vaccino")
        label.setStyleSheet("border-radius: 20px; border: 2px solid purple;")
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

        if self.controller.get_is_doppia_dose_vaccino:
            label_monodose = QLabel("Dosi previste: 2")
        else:
            label_monodose = QLabel("Dosi previste: 1")
        font_monodose = label_monodose.font()
        font_monodose.setPointSize(16)
        font_monodose.setFamily('Georgia')
        font_monodose.setItalic(True)
        label_monodose.setFont(font_monodose)
        v_layout.addWidget(label_monodose)

        label_distanza = QLabel("Giorni di distanza tra le due dosi: {}".format(self.controller.get_distanza_seconda_dose_vaccino()))
        font_distanza = label_distanza.font()
        font_distanza.setPointSize(16)
        font_distanza.setFamily('Georgia')
        font_distanza.setItalic(True)
        label_distanza.setFont(font_distanza)
        v_layout.addWidget(label_distanza)

        self.setWindowTitle("Vaccino " + self.controller.get_tipologia_materiale())
        self.setWindowIcon(QIcon('appuntamentovaccino/data/CovidFree_Clinica.png'))
        self.setLayout(v_layout)

        self.setMaximumSize(400, 300)
        self.resize(400, 300)
        self.move(250, 190)

