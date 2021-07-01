from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QMessageBox, QPushButton, QRadioButton, QGridLayout

from appuntamentotampone.view.VistaAppuntamentoTampone import VistaAppuntamentoTampone
from calendariotamponi.controller.ControlloreCalendarioTamponi import ControlloreCalendarioTamponi


class VistaRicercaAppuntamentoTampone(QWidget):

    def __init__(self, parent=None):
        super(VistaRicercaAppuntamentoTampone, self).__init__(parent)

        self.controller = ControlloreCalendarioTamponi()
        self.info = {}

        self.v_layout = QVBoxLayout()

        self.get_parametri_di_ricerca("Nome:")
        self.get_parametri_di_ricerca("Cognome:")
        self.get_parametri_di_ricerca("Data di nascita:")
        self.get_parametri_di_ricerca("Codice fiscale:")

        self.label = QLabel("Appuntamento per:")
        font = QFont("Georgia", 12)
        self.label.setFont(font)
        self.v_layout.addWidget(self.label)

        self.antigenico = QRadioButton('Antigenico Rapido')
        self.molecolare = QRadioButton('Molecolare')
        self.sierologico = QRadioButton('Sierologico')

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.antigenico, 0, 0)
        grid_layout.addWidget(self.molecolare, 0, 1)
        grid_layout.addWidget(self.sierologico, 0, 2)
        self.v_layout.addLayout(grid_layout)

        btn = QPushButton("OK")
        btn.clicked.connect(self.ricerca_appuntamento)
        self.v_layout.addWidget(btn)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Ricerca appuntamento")
        self.setWindowIcon(QIcon('appuntamentovaccino/data/CovidFree_Clinica.png'))

        self.setMaximumSize(400, 300)
        self.resize(500, 200)
        self.move(170, 200)

    def get_parametri_di_ricerca(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QLineEdit(self)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    def ricerca_appuntamento(self):
        nome = self.info["Nome:"].text()
        cognome = self.info["Cognome:"].text()
        data_di_nascita = self.info["Data di nascita:"].text()
        cf = self.info["Codice fiscale:"].text()

        ok = True
        if nome == "" or cognome == "" or data_di_nascita == "" or cf == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, completa tutti i campi', QMessageBox.Ok, QMessageBox.Ok)
            ok = False

        if ok is True:
            if self.antigenico.isChecked():
                tipo_tampone = self.antigenico.text()
            elif self.molecolare.isChecked():
                tipo_tampone = self.molecolare.text()
            elif self.sierologico.isChecked():
                tipo_tampone = self.sierologico.text()
            else:
                QMessageBox.critical(self, 'Errore', 'Per favore, indicare quale appuntamento si vuole ricercare', QMessageBox.Ok, QMessageBox.Ok)
                ok = False

        if ok is True:
            appuntamento_ricercato = self.controller.get_appuntamento_by_cf(nome, cognome, data_di_nascita, cf, tipo_tampone)

            if appuntamento_ricercato is None:
                QMessageBox.warning(self, 'Attenzione', 'Siamo spiacenti ma nessun appuntamento corrisponde ai paramenti inseriti',
                                     QMessageBox.Ok, QMessageBox.Ok)
            else:
                self.vista_ricerca = VistaAppuntamentoTampone(appuntamento_ricercato)
                self.vista_ricerca.show()
                self.close()


