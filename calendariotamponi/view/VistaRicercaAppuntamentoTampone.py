import datetime

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QMessageBox, QPushButton

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

        btn = QPushButton("OK")
        btn.clicked.connect(self.ricerca_appuntamento)
        self.v_layout.addWidget(btn)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Ricerca appuntamento")

    def get_parametri_di_ricerca(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QLineEdit(self)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    def ricerca_appuntamento(self):
        nome = self.info["Nome:"].text()
        cognome = self.info["Cognome:"].text()
        data_di_nascita = self.info["Data di nascita:"].text()

        ok = True
        if nome == "" or cognome == "" or data_di_nascita == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, completa tutti i campi', QMessageBox.Ok, QMessageBox.Ok)
            ok = False

        if ok is True:
            appuntamento_ricercato = self.controller.get_appuntamento(nome,cognome,data_di_nascita)

            if appuntamento_ricercato is None:
                QMessageBox.warning(self, 'Attenzione', 'Siamo spiacenti ma nessun appuntamento corrisponde ai paramenti inseriti',
                                     QMessageBox.Ok, QMessageBox.Ok)
            else:
                self.vista_ricerca = VistaAppuntamentoTampone(appuntamento_ricercato)
                self.vista_ricerca.show()
                self.close()


