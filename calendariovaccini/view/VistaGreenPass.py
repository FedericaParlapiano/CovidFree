from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QSpacerItem, QSizePolicy, QHBoxLayout

from calendariovaccini.controller.ControlloreCalendarioVaccini import ControlloreCalendarioVaccini


class VistaGreenPass(QWidget):

    def __init__(self, appuntamento, parent = None):
        super(VistaGreenPass, self).__init__(parent)
        self.controller = ControlloreCalendarioVaccini()

        v_layout = QVBoxLayout()
        v_layout_l =QVBoxLayout()
        h_layout = QHBoxLayout()

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        pixmap = QPixmap('appuntamentovaccino/data/qrcode.png')
        pixmap5 = pixmap.scaled(120, 120)
        pixmap.size()
        label_im = QLabel()
        label_im.setPixmap(pixmap5)
        label_im.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label_im)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_nome1 = QLabel("Cognome e Nome")
        font_nome1 = label_nome1.font()
        font_nome1.setPointSize(14)
        font_nome1.setFamily('Georgia')
        font_nome1.setBold(True)
        label_nome1.setFont(font_nome1)
        v_layout.addWidget(label_nome1)

        label_nome2 = QLabel("Surname(s) and forename(s)".format(appuntamento.cartella_paziente.nome, appuntamento.cartella_paziente.cognome))
        font_nome2 = label_nome2.font()
        font_nome2.setPointSize(10)
        font_nome2.setFamily('Georgia')
        label_nome2.setFont(font_nome2)
        v_layout.addWidget(label_nome2)

        label_nome3 = QLabel(appuntamento.cartella_paziente.cognome + " " + appuntamento.cartella_paziente.nome)
        font_nome3 = label_nome3.font()
        font_nome3.setPointSize(20)
        font_nome3.setFamily('Georgia')
        font_nome3.setCapitalization(True)
        label_nome3.setFont(font_nome3)
        v_layout.addWidget(label_nome3)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_data_nascita1 = QLabel("Data di nascita")
        font_data_nascita1 = label_data_nascita1.font()
        font_data_nascita1.setPointSize(14)
        font_data_nascita1.setFamily('Georgia')
        label_data_nascita1.setFont(font_data_nascita1)
        v_layout.addWidget(label_data_nascita1)

        label_data_nascita2 = QLabel("Date of birth(yyyy-mm-dd)")
        font_data_nascita2 = label_data_nascita2.font()
        font_data_nascita2.setPointSize(10)
        font_data_nascita2.setFamily('Georgia')
        label_data_nascita2.setFont(font_data_nascita2)
        v_layout.addWidget(label_data_nascita2)

        label_data_nascita3 = QLabel(appuntamento.cartella_paziente.data_di_nascita)
        font_data_nascita3 = label_data_nascita3.font()
        font_data_nascita3.setPointSize(20)
        font_data_nascita3.setFamily('Georgia')
        label_data_nascita3.setFont(font_data_nascita3)
        v_layout.addWidget(label_data_nascita3)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_cf1 = QLabel("Identificativo univoco del certificato")
        font_cf1 = label_cf1.font()
        font_cf1.setPointSize(14)
        font_cf1.setFamily('Georgia')
        label_cf1.setFont(font_cf1)
        v_layout.addWidget(label_cf1)

        label_cf2 = QLabel("Unique Certificate Identifier")
        font_cf2 = label_cf2.font()
        font_cf2.setPointSize(10)
        font_cf2.setFamily('Georgia')
        label_cf2.setFont(font_cf2)
        v_layout.addWidget(label_cf2)

        label_cf3 = QLabel(appuntamento.cartella_paziente.cf)
        font_cf3 = label_cf3.font()
        font_cf3.setPointSize(20)
        font_cf3.setFamily('Georgia')
        label_cf3.setFont(font_cf3)
        v_layout.addWidget(label_cf3)

        label_europa = QLabel("Certificazione verde \n COVID-19 \n EU Digital \n COVID Certificate")
        font_europa = label_europa.font()
        font_europa.setPointSize(20)
        font_europa.setFamily('Georgia')
        font_europa.setBold(True)
        label_europa.setFont(font_europa)
        label_europa.setAlignment(Qt.AlignCenter)
        v_layout_l.addWidget(label_europa)
        
        pixmap_eu = QPixmap('appuntamentovaccino/data/europa.png')
        pixmap2 = pixmap_eu.scaled(180, 120)
        label_eu = QLabel()
        label_eu.setPixmap(pixmap2)
        label_eu.setAlignment(Qt.AlignCenter)
        v_layout_l.addWidget(label_eu)

        h_layout.addLayout(v_layout)
        h_layout.addItem(QSpacerItem(50, 50, QSizePolicy.Minimum, QSizePolicy.Expanding))
        h_layout.addLayout(v_layout_l)

        self.setLayout(h_layout)