from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from materiale.controller.ControlloreMateriale import ControlloreMateriale


class VistaAggiornaFornitura(QWidget):

    def __init__(self, materiale, aggiornamento, callback_aggiornamento, parent=None):
        super(VistaAggiornaFornitura, self).__init__(parent)
        self.controller = ControlloreMateriale(materiale)
        self.aggiornamento = aggiornamento
        self.callback_aggiornamento = callback_aggiornamento

        v_layout = QVBoxLayout()

        label_fornitura = QLabel("Inserisci la quantità del vaccino da aggiungere al magazzino:")
        font_fornitura = label_fornitura.font()
        font_fornitura.setPointSize(16)
        font_fornitura.setFamily('Georgia')
        font_fornitura.setItalic(True)
        label_fornitura.setFont(font_fornitura)
        v_layout.addWidget(label_fornitura)

        self.nuova_quantita = QLineEdit(self)
        v_layout.addWidget(self.nuova_quantita)

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.aggiorna_quantita)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.setWindowTitle("Aggiornamento della fornitura di " + self.controller.get_tipologia_materiale())

    def aggiorna_quantita(self):
        if self.nuova_quantita.text() == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci la quantita della fornitura', QMessageBox.Ok, QMessageBox.Ok)
        else:
            print(self.nuova_quantita.text())
            self.aggiornamento(self.controller.get_tipologia_materiale(), self.nuova_quantita.text())
            self.callback_aggiornamento()
            self.close()