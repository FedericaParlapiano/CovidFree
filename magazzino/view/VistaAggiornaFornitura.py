from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from materiale.controller.ControlloreMateriale import ControlloreMateriale


class VistaAggiornaFornitura(QWidget):

    def __init__(self, materiale, aggiornamento, callback_aggiornamento, parent=None):
        super(VistaAggiornaFornitura, self).__init__(parent)
        self.controller = ControlloreMateriale(materiale)
        self.aggiornamento = aggiornamento
        self.callback_aggiornamento = callback_aggiornamento

        v_layout = QVBoxLayout()
        label_fornitura = QLabel("Inserisci la quantità del materiale da aggiungere al magazzino:")
        v_layout.addWidget(label_fornitura)

        self.nuova_quantita = QLineEdit(self)
        v_layout.addWidget(self.nuova_quantita)

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.aggiorna_quantita)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.setFont(QFont('Arial Nova Light', 13))
        self.setWindowTitle("Aggiornamento della fornitura di " + materiale.tipologia)
        self.setWindowIcon(QIcon('appuntamentovaccino/data/CovidFree_Clinica.png'))

        self.setMaximumSize(600, 100)
        self.resize(600, 100)
        self.move(70, 250)

    def aggiorna_quantita(self):
        ok = True
        if self.nuova_quantita.text() == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci la quantita della fornitura', QMessageBox.Ok, QMessageBox.Ok)
            ok = False
        if ok is True:
            try:
                quantita = int(self.nuova_quantita.text())
            except:
                QMessageBox.critical(self, 'Errore', 'Il formato inserito non è valido', QMessageBox.Ok, QMessageBox.Ok)
                ok = False
        if ok is True and quantita > 0:
            self.aggiornamento(self.controller.get_tipologia_materiale(), quantita)
            self.callback_aggiornamento()
            self.close()

