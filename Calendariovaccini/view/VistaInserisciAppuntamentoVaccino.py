from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QLabel, QLineEdit, QMessageBox


class VistaInserisciAppuntamentoVaccino(QWidget):

    def __init__(self, controller, callback):
        super(VistaInserisciAppuntamentoVaccino, self).__init__()
        self.controller = controller
        self.callback = callback
        self.info = {}

        self.v_layout = QVBoxLayout()

        self.get_form_entry("Nome")
        self.get_form_entry("Cognome")
        self.get_form_entry("Data di nascita")
        self.get_form_entry("Codice Fiscale")
        self.get_form_entry("Indirizzo")
        self.get_form_entry("Telefono")
        self.get_form_entry("Patologie")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_appuntamento)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Appuntamento")

    def get_form_entry(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QLineEdit(self)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    def add_appuntamento(self):
        nome = self.info["Nome"].text()
        cognome = self.info["Cognome"].text()
        data_nascita = self.info["Data di nascita"].text()
        cf = self.info["Codice Fiscale"].text()
        indirizzo = self.info["Indirizzo"].text()
        telefono = self.info["Telefono"].text()
        patologie = self.info["Patologie"].text()
        if nome == "" or cognome == "" or data_nascita == "" or cf == "" or indirizzo == ""  or telefono == "" or patologie == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)
        else:
            #self.controller.aggiungi_cliente(Cliente((nome+cognome).lower(), nome, cognome, cf, indirizzo, email, telefono, eta))
            self.callback()
            self.close()
