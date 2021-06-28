from datetime import date, datetime, timedelta

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QLabel, QLineEdit, QMessageBox, \
    QGridLayout, QCheckBox, QRadioButton, QComboBox

from appuntamentovaccino.model.AppuntamentoVaccino import AppuntamentoVaccino
from appuntamentovaccino.view.VistaAppuntamentoVaccino import VistaAppuntamentoVaccino
from calendariovaccini.controller.ControlloreCalendarioVaccini import ControlloreCalendarioVaccini
from calendariovaccini.view.VistaDateAppuntamento import VistaDateAppuntamento
from calendariovaccini.view.VistaInserisciAnamnesi import VistaInserisciAnamnesi
from cartellapaziente.model.CartellaPaziente import CartellaPaziente


class VistaModificaAppuntamentoVaccino(QWidget):

    def __init__(self, appuntamento):
        super(VistaModificaAppuntamentoVaccino, self).__init__()
        self.controller = ControlloreCalendarioVaccini()
        self.appuntamento = appuntamento
        self.info = {}
        self.vista_inserisci_anamnesi = VistaInserisciAnamnesi(self.controller, self.update_ui)
        self.vista_mostra_date = VistaDateAppuntamento()

        self.v_layout = QVBoxLayout()


        self.get_form_entry("Nome*", self.appuntamento.cartella_paziente.nome)
        self.get_form_entry("Cognome*", self.appuntamento.cartella_paziente.cognome)
        self.get_form_entry("Data di nascita (dd/mm/YYYY)*", self.appuntamento.cartella_paziente.data_di_nascita)
        self.get_form_entry("Codice Fiscale*", self.appuntamento.cartella_paziente.cf)
        self.get_form_entry("Indirizzo*", self.appuntamento.cartella_paziente.indirizzo)
        self.get_form_entry("Telefono*", self.appuntamento.cartella_paziente.telefono)
        self.domicilio = QCheckBox("L'appuntamento è a domicilio")
        self.v_layout.addWidget(self.domicilio)

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.v_layout.addWidget(QLabel("Categorie speciali"))
        self.categorie_speciali = QComboBox()
        self.categorie_speciali.addItems([" ", "Medici e Infermieri (personale sanitario)", "Membri delle Forze Armate", "Persone con comorbidità", "Persone che assistono individui fragili"])
        self.v_layout.addWidget(self.categorie_speciali)
        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        button = QPushButton("Anamnesi*")
        button.clicked.connect(self.go_inserisci_anamnesi)
        self.v_layout.addWidget(button)
        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.v_layout.addWidget(QLabel("Preferenza (opzionale)"))
        self.preferenza = QComboBox()
        self.preferenza.addItems([" ", "Pfizer", "Moderna", "Astrazeneca"])
        self.v_layout.addWidget(self.preferenza)
        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        button_data = QPushButton("Scegli data e orario*")
        button_data.clicked.connect(self.go_scelta_data)
        self.v_layout.addWidget(button_data)
        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.consenso1 = QCheckBox("Consenso al trattamento dei dati personali*")
        self.v_layout.addWidget(self.consenso1)
        self.consenso2 = QCheckBox("Consenso al trattamento sanitario*")
        self.v_layout.addWidget(self.consenso2)
        self.v_layout.addItem(QSpacerItem(40, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.v_layout.addWidget(QLabel("* Campi Obbligatori"))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_appuntamento)
        self.v_layout.addWidget(btn_ok)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Modifica Appuntamento")
        self.resize(300,600)

    def get_form_entry(self, tipo, campo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QLineEdit(self)
        current_text_edit.setText(campo)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    def go_inserisci_anamnesi(self):
        self.vista_inserisci_anamnesi.show()

    def go_scelta_data(self):
        self.vista_mostra_date.show()


    def add_appuntamento(self):
        nome = self.info["Nome*"].text()
        cognome = self.info["Cognome*"].text()
        data_nascita = self.info["Data di nascita (dd/mm/YYYY)*"].text()
        cf = self.info["Codice Fiscale*"].text()
        indirizzo = self.info["Indirizzo*"].text()
        telefono = self.info["Telefono*"].text()
        preferenze = self.preferenza.currentText()
        categoria_speciale = self.categorie_speciali.currentText()
        is_a_domicilio = False
        if self.domicilio.isChecked():
            is_a_domicilio = True

        ok = True

        if nome == "" or cognome == "" or data_nascita == "" or cf == "" or indirizzo == "" or telefono == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, completa tutti i campi', QMessageBox.Ok, QMessageBox.Ok)
            ok = False

        if ok is True:
            try:
                data_inserita = datetime.strptime(self.info["Data di nascita (dd/mm/YYYY)*"].text(),'%d/%m/%Y')
            except:
                QMessageBox.critical(self, 'Errore', 'Inserisci la data nel formato richiesto: dd/MM/yyyy',
                                     QMessageBox.Ok, QMessageBox.Ok)
                ok = False

            if ok is True and date.today().year - data_inserita.year < 0:
                QMessageBox.critical(self, 'Errore', 'La data inserita non è valida',
                                     QMessageBox.Ok, QMessageBox.Ok)
                ok = False

            if ok is True and date.today().year - data_inserita.year < 16:
                QMessageBox.critical(self, 'Errore',
                                     'Per i minori di 16 anni non è prevista la possibilità di prenotarsi per la vaccinazione',
                                     QMessageBox.Ok, QMessageBox.Ok)
                ok = False

            if ok is True and categoria_speciale == ' ' and date.today().year - data_inserita.year < 50:
                QMessageBox.critical(self, 'Errore', 'Attualmente le direttive nazionali non permettono la prenotazione a coloro che hanno '
                                                     'un\'età inferiore ai 50 anni e non rientrano in una delle categorie con priorità', QMessageBox.Ok, QMessageBox.Ok)
                ok = False

        if ok is True:
            if not bool(self.vista_inserisci_anamnesi.anamnesi):
                QMessageBox.critical(self, 'Errore', 'Non è stata compilato il questionario anamnestico!', QMessageBox.Ok, QMessageBox.Ok)
                ok = False

        if ok is True and (self.consenso1.isChecked() is False or self.consenso2.isChecked() is False):
            ok = False
            QMessageBox.critical(self, 'Errore', 'Se non viene fornito il consenso non è possibile procedere '
                                                 'con la prenotazione', QMessageBox.Ok, QMessageBox.Ok)

        if ok is True:
            if self.vista_inserisci_anamnesi.anamnesi['Pfizer']=='Sì' and self.vista_inserisci_anamnesi.anamnesi['Moderna']=='Sì' and self.vista_inserisci_anamnesi.anamnesi['Astrazeneca']=="Sì":
                QMessageBox.critical(self, 'Attenzione', 'Ci dispiace ma al momento non sono disponibili'
                                                        ' vaccini che non le provichino reazioni allergiche. Non è possibile procedere con la prenotazione!', QMessageBox.Ok, QMessageBox.Ok)
                ok = False
            elif self.vista_inserisci_anamnesi.anamnesi['Contatto']=='Sì' or self.vista_inserisci_anamnesi.anamnesi['Sintomi']=='Sì':
                QMessageBox.critical(self, 'Attenzione', 'Ci dispiace ma non è possibile prenotare '
                                                       'l\'appuntamento se si presentano sintomi ricondubili ad un\'infezione da Covid19 o se si è stati a contatto con persone positive.', QMessageBox.Ok, QMessageBox.Ok)
                ok = False

        if ok is True:
            if self.vista_inserisci_anamnesi.anamnesi['Positivo COVID-19'] == 'meno di 3 mesi':
                QMessageBox.critical(self, 'Attenzione', 'Ci dispiace ma non è possibile prenotare '
                                                         'l\'appuntamento se non è passato un periodo superiore ai 3 mesi dall\'infezione.',
                                     QMessageBox.Ok, QMessageBox.Ok)
                ok = False

        if ok is True:
            if self.vista_mostra_date.data_scelta == "" or  self.vista_mostra_date.orario_selezionato == "":
                QMessageBox.critical(self, 'Errore', 'Non è stata scelta una data per l\'appuntamento!', QMessageBox.Ok,
                                 QMessageBox.Ok)
                ok = False

        if ok is True:
            self.controller.elimina_appuntamento(self.controller.get_appuntamento(self.appuntamento.cartella_paziente.nome, self.appuntamento.cartella_paziente.cognome, self.appuntamento.id))
            cartella_paziente = CartellaPaziente(nome, cognome, data_nascita, cf, indirizzo, telefono,
                                                 categoria_speciale, preferenze, self.vista_inserisci_anamnesi.anamnesi)
            self.appuntamento_vaccino = AppuntamentoVaccino(self.appuntamento.id, cartella_paziente,
                                                       self.vista_mostra_date.data_scelta,
                                                       self.vista_mostra_date.orario_selezionato, is_a_domicilio)

            if self.appuntamento_vaccino.vaccino is not None:
                self.controller.aggiungi_appuntamento(self.appuntamento_vaccino)

                if self.appuntamento.id == 'Prima Dose':
                    seconda_dose = self.controller.get_appuntamento(self.appuntamento.cartella_paziente.nome, self.appuntamento.cartella_paziente.cognome, 'Seconda Dose')
                    if seconda_dose is not None:
                        self.controller.elimina_appuntamento(seconda_dose)
                    if self.vista_inserisci_anamnesi.anamnesi['Positivo COVID-19'] != 'tra i 3 e i 6 mesi':
                        data_prima_dose = datetime.strptime(self.vista_mostra_date.data_scelta, '%d-%m-%Y')
                        if self.appuntamento_vaccino.vaccino == "Pfizer":
                            data_seconda_dose = str((data_prima_dose + timedelta(days=28)).strftime('%d-%m-%Y'))
                        elif self.appuntamento_vaccino.vaccino == "Moderna":
                            data_seconda_dose = str((data_prima_dose + timedelta(days=21)).strftime('%d-%m-%Y'))
                        elif self.appuntamento_vaccino.vaccino == "Astrazeneca":
                            data_seconda_dose = str((data_prima_dose + timedelta(days=60)).strftime('%d-%m-%Y'))

                        appuntamento_seconda_dose = AppuntamentoVaccino('Seconda Dose', cartella_paziente,
                                                                        data_seconda_dose,
                                                                        self.vista_mostra_date.orario_selezionato,
                                                                        is_a_domicilio)
                        self.controller.aggiungi_appuntamento(appuntamento_seconda_dose)
                        self.vista_riepilogo_2 = VistaAppuntamentoVaccino(appuntamento_seconda_dose)
                        self.vista_riepilogo_2.show()

                self.vista_riepilogo = VistaAppuntamentoVaccino(self.appuntamento_vaccino)
                self.vista_riepilogo.show()
            else:
                QMessageBox.critical(self, 'Errore', 'Ci dispiace ma non è possibile prenotare '
                                                         'l\'appuntamento a causa di una mancanza di vaccini che possono essere somministrati al paziente.',
                                     QMessageBox.Ok, QMessageBox.Ok)
            self.close()

    def update_ui(self):
        pass