from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QSpacerItem, QSizePolicy

from calendariovaccini.controller.ControlloreCalendarioVaccini import ControlloreCalendarioVaccini


class VistaGreenPass(QWidget):

    def __init__(self, appuntamento, parent = None):
        super(VistaGreenPass, self).__init__(parent)
        self.controller = ControlloreCalendarioVaccini()

        v_layout = QVBoxLayout()

        label_nome = QLabel("Nome e cognome: {} {}".format(appuntamento.cartella_paziente.nome, appuntamento.cartella_paziente.cognome))
        font_nome = label_nome.font()
        font_nome.setPointSize(20)
        font_nome.setFamily('Georgia')
        font_nome.setItalic(True)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_tipo = QLabel("Tipo vaccino: {}".format(appuntamento.vaccino))
        font_tipo = label_tipo.font()
        font_tipo.setPointSize(18)
        font_tipo.setFamily('Georgia')
        label_tipo.setFont(font_tipo)
        label_tipo.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label_tipo)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        pixmap = QPixmap('appuntamentovaccino/data/qrcode.png')
        pixmap5 = pixmap.scaled(100, 30)
        pixmap.size()
        label_im = QLabel()
        label_im.setPixmap(pixmap5)
        label_im.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label_im)

        label_cf = QLabel("Codice fiscale: {}".format(appuntamento.cartella_paziente.cf))
        font_cf = label_cf.font()
        font_cf.setPointSize(12)
        font_cf.setFamily('Georgia')
        label_cf.setFont(font_cf)
        v_layout.addWidget(label_cf)

        label_indirizzo = QLabel("Indirizzo: {}".format(appuntamento.cartella_paziente.indirizzo))
        font_indirizzo = label_indirizzo.font()
        font_indirizzo.setPointSize(12)
        font_indirizzo.setFamily('Georgia')
        label_indirizzo.setFont(font_indirizzo)
        v_layout.addWidget(label_indirizzo)

        label_data_nascita = QLabel("Data di nascita: {}".format(appuntamento.cartella_paziente.data_di_nascita))
        font_data_nascita = label_data_nascita.font()
        font_data_nascita.setPointSize(12)
        font_data_nascita.setFamily('Georgia')
        label_data_nascita.setFont(font_data_nascita)
        v_layout.addWidget(label_data_nascita)

        self.setLayout(v_layout)