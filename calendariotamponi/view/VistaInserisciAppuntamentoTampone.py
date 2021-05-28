from datetime import date, datetime
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QCheckBox, QSpacerItem, QSizePolicy, QLabel, QComboBox, QLineEdit, \
    QPushButton, QMessageBox

class VistaInserisciAppuntamentoTampone(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciAppuntamentoTampone, self).__init__()
        self.controller = controller
        self.callback = callback
        self.info = {}
        self.v_layout = QVBoxLayout()

        self.get_form_entry("Nome")
        self.get_form_entry("Cognome")
        self.get_form_entry("Data di nascita (dd/mm/YYYY)")
        self.get_form_entry("Codice Fiscale")
        self.get_form_entry("Indirizzo")
        self.get_form_entry("Telefono")
        self.get_form_entry("Data appuntamento")

        self.drive_through = QCheckBox("Presenta sintomi o ha avuto contatti con persone positive o è attualmente positivo")
        self.v_layout.addWidget(self.drive_through)
        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.v_layout.addWidget(QLabel("Tipologia di tampone da effettuare"))
        self.tipo_tampone = QComboBox()
        self.tipo_tampone.addItems([" ", "Antigenico rapido", "Molecolare", "Sierologico"])
        self.v_layout.addWidget(self.tipo_tampone)
        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.setLayout(self.v_layout)

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_appuntamento)
        self.v_layout.addWidget(btn_ok)
        self.setWindowTitle("Nuovo Appuntamento")



    def get_form_entry(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QLineEdit(self)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    def add_appuntamento(self):
        nome = self.info["Nome"].text()
        cognome = self.info["Cognome"].text()
        data_nascita = self.info["Data di nascita (dd/mm/YYYY)"].text()
        cf = self.info["Codice Fiscale"].text()
        indirizzo = self.info["Indirizzo"].text()
        telefono = self.info["Telefono"].text()
        tipo_tampone = self.tipo_tampone.currentText()

        ok = True

        if nome == "" or cognome == "" or data_nascita == "" or cf == "" or indirizzo == "" or telefono == "" or tipo_tampone == ' ':
            QMessageBox.critical(self, 'Errore', 'Per favore, completa tutti i campi', QMessageBox.Ok, QMessageBox.Ok)
            ok = False

        if ok is True:
            try:
                data_inserita = datetime.strptime(self.info["Data di nascita (dd/mm/YYYY)"].text(), '%d/%m/%Y')
            except:
                QMessageBox.critical(self, 'Errore', 'Inserisci la data nel formato richiesto: dd/MM/yyyy',
                                     QMessageBox.Ok, QMessageBox.Ok)
                ok = False

        if ok is True:
            is_drive_through = False
            if self.drive_through.isChecked():
                is_drive_through = True












