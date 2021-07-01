from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QRadioButton, QLabel, QGridLayout, QVBoxLayout, QLineEdit, QMessageBox, QPushButton

from appuntamentovaccino.view.VistaAppuntamentoVaccino import VistaAppuntamentoVaccino
from calendariovaccini.controller.ControlloreCalendarioVaccini import ControlloreCalendarioVaccini


class VistaRicercaAppuntamentoVaccino(QWidget):

    def __init__(self, parent=None):
        super(VistaRicercaAppuntamentoVaccino, self).__init__(parent)

        self.controller = ControlloreCalendarioVaccini()
        self.info = {}

        self.v_layout = QVBoxLayout()

        self.get_parametri_di_ricerca("Nome:")
        self.get_parametri_di_ricerca("Cognome:")
        self.get_parametri_di_ricerca("Codice fiscale:")

        self.label = QLabel("Appuntamento per:")
        self.v_layout.addWidget(self.label)

        self.prima_dose = QRadioButton('Prima Dose')
        self.seconda_dose = QRadioButton('Seconda Dose')

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.prima_dose, 0, 0)
        grid_layout.addWidget(self.seconda_dose, 0, 1)
        self.v_layout.addLayout(grid_layout)

        btn = QPushButton("OK")
        btn.clicked.connect(self.ricerca_appuntamento)
        self.v_layout.addWidget(btn)

        self.setLayout(self.v_layout)
        self.setFont(QFont('Arial Nova Light', 12))
        self.setWindowTitle("Ricerca appuntamento")
        self.setWindowIcon(QIcon('appuntamentovaccino/data/CovidFree_Clinica.png'))

        self.setMaximumSize(400, 300)
        self.resize(400, 300)
        self.move(170, 200)

    def get_parametri_di_ricerca(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QLineEdit(self)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    def ricerca_appuntamento(self):
        nome = self.info["Nome:"].text()
        cognome = self.info["Cognome:"].text()
        cf = self.info["Codice fiscale:"].text()

        ok = True
        if nome == "" or cognome == "" or cf == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, completa tutti i campi', QMessageBox.Ok, QMessageBox.Ok)
            ok = False

        if ok is True:
            if self.prima_dose.isChecked():
                tipo_appuntamento = self.prima_dose.text()
            elif self.seconda_dose.isChecked():
                tipo_appuntamento = self.seconda_dose.text()
            else:
                QMessageBox.critical(self, 'Errore', 'Per favore, indicare quale appuntamento si vuole ricercare', QMessageBox.Ok, QMessageBox.Ok)
                ok = False

        if ok is True:
            appuntamento_ricercato = self.controller.get_appuntamento_by_cf(nome, cognome, cf, tipo_appuntamento)

            if appuntamento_ricercato is None:
                QMessageBox.warning(self, 'Attenzione', 'Siamo spiacenti ma nessun appuntamento corrisponde ai paramenti inseriti',
                                     QMessageBox.Ok, QMessageBox.Ok)
            else:
                self.vista_ricerca = VistaAppuntamentoVaccino(appuntamento_ricercato)
                self.vista_ricerca.show()
                self.close()


