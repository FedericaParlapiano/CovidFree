import calendar
import os
import pickle
from datetime import date, datetime
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QCheckBox, QSpacerItem, QSizePolicy, QLabel, QComboBox, QLineEdit, \
    QPushButton, QMessageBox, QCalendarWidget, QListView, QGridLayout, QAbstractItemView
from appuntamentotampone.model.AppuntamentoTampone import AppuntamentoTampone

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

        self.data_selezionata = " "
        self.orario_selected = " "
        self.calendar_layout = QGridLayout()
        self.calendario_appuntamento = self.init_calendario()

        self.calendar_layout.addWidget(QLabel("Data appuntamento"), 0, 0)
        self.calendar_layout.addWidget(self.calendario_appuntamento, 1, 0)

        self.calendario_appuntamento.selectionChanged.connect(self.calendar_date)

        self.label = QLabel('')
        self.label_orario = QLabel('')
        self.calendar_layout.addWidget(QLabel("Fascia oraria appuntamento"), 0, 1)

        self.list_view_orario = QListView()

        self.update_ui()

        self.calendar_layout.addWidget(self.list_view_orario, 1, 1)

        self.list_view_orario.selectionModel().currentChanged.connect(self.show_selected_orario)

        self.calendar_layout.addWidget(self.label, 2, 0)
        self.calendar_layout.addWidget(self.label_orario, 2, 1)
        self.v_layout.addLayout(self.calendar_layout)

        self.drive_through = QCheckBox("Presenta sintomi o ha avuto contatti con persone positive o è attualmente positivo")

        self.v_layout.addWidget(self.drive_through)
        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.v_layout.addWidget(QLabel("Tipologia di tampone da effettuare"))
        self.tipo_tampone = QComboBox()
        self.tipo_tampone.addItems([" ", "Antigenico Rapido", "Molecolare", "Sierologico"])

        self.v_layout.addWidget(self.tipo_tampone)
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
        data_nascita = self.info["Data di nascita (dd/mm/YYYY)"].text()
        cf = self.info["Codice Fiscale"].text()
        indirizzo = self.info["Indirizzo"].text()
        telefono = self.info["Telefono"].text()
        tipo_tampone = self.tipo_tampone.currentText()
        ok = True
        if nome == "" or cognome == "" or data_nascita == "" or cf == "" or indirizzo == "" or telefono == "" or tipo_tampone == ' ' or self.orario_selected == " " or self.data_selezionata == " ":
            QMessageBox.critical(self, 'Errore', 'Per favore, completa tutti i campi', QMessageBox.Ok, QMessageBox.Ok)
            ok = False
        if ok is True:
            try:
                data_inserita = datetime.strptime(self.info["Data di nascita (dd/mm/YYYY)"].text(), '%d/%m/%Y')
            except:
                QMessageBox.critical(self, 'Errore', 'Inserisci la data nel formato richiesto: dd/MM/yyyy',
                                     QMessageBox.Ok, QMessageBox.Ok)
                ok = False
        if ok is True and date.today().year < data_inserita.year:
            QMessageBox.critical(self, 'Errore', 'La data di nascita inserita non è valida',
                                 QMessageBox.Ok, QMessageBox.Ok)
            ok = False
        #d = datetime.strptime(self.data_selezionata, '%Y-%m-%d')
        if ok is True:
            d = datetime.strptime(self.data_selezionata, '%Y-%m-%d')
            if date.today().day > d.day and date.today().month == d.month:
                QMessageBox.critical(self, 'Errore', 'La data selezionata per l\' appuntamento non è valida',
                                     QMessageBox.Ok, QMessageBox.Ok)
                ok = False
        if ok is True and not self.controllo_disponibilita():
            QMessageBox.critical(self, 'Errore', 'Siamo spiacenti, ma attualmente non è disponibile la tipologia di tampone selezionata',
                                 QMessageBox.Ok, QMessageBox.Ok)
            ok = False
        if ok is True:
            contatore_data = 0
            contatore_ora = 0
            for appuntamento in self.controller.get_elenco_appuntamenti():
                if appuntamento.data_appuntamento == self.data_selezionata:
                    contatore_data = contatore_data + 1
                    if appuntamento.fascia_oraria == self.orario_selected:
                        contatore_ora = contatore_ora + 1
            if contatore_data > 39:
                QMessageBox.critical(self, 'Errore', 'Siamo spiacenti, il giorno selezionata è al completo.', QMessageBox.Ok, QMessageBox.Ok)
                ok = False
            elif contatore_ora > 3:
                QMessageBox.critical(self, 'Errore', 'Siamo spiacenti, la fascia oraria selezionata è al completo.', QMessageBox.Ok, QMessageBox.Ok)
                ok = False
        if ok is True:
            d = datetime.strptime(self.data_selezionata, '%Y-%m-%d')
            is_drive_through = False
            if self.drive_through.isChecked():
                is_drive_through = True
            self.controller.aggiungi_appuntamento(AppuntamentoTampone(nome, cognome, cf, telefono, indirizzo, data_nascita, self.data_selezionata, self.orario_selected, is_drive_through, tipo_tampone))
            self.close()

    def controllo_disponibilita(self):
        disponibile = False
        if os.path.isfile('magazzino/data/lista_tamponi_salvata.pickle'):
            with open('magazzino/data/lista_tamponi_salvata.pickle', 'rb') as f:
                self.tamponi_presenti = pickle.load(f)
        for tampone in self.tamponi_presenti:
            if tampone.tipologia == self.tipo_tampone.currentText() and tampone.is_disponibile():
                disponibile = True
                tampone.quantita = tampone.quantita - 1
                with open('magazzino/data/lista_tamponi_salvata.pickle', 'wb') as handle:
                    pickle.dump(self.tamponi_presenti, handle, pickle.HIGHEST_PROTOCOL)
        return disponibile

    def init_calendario(self):
        calendario = QCalendarWidget(self)
        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        calendario.setMinimumDate(QDate(currentYear, currentMonth, 1))
        calendario.setMaximumDate(
            QDate(currentYear + 1, currentMonth, calendar.monthrange(currentYear, currentMonth)[1]))
        calendario.setSelectedDate(QDate(currentYear, currentMonth, 1))
        calendario.setFont(QFont('Georgia', 10))
        calendario.setStyleSheet('background-color: lightblue')
        calendario.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        calendario.setGeometry(200, 200, 300, 200)
        calendario.setGridVisible(True)
        return calendario

    def calendar_date(self):
        dateselected = self.calendario_appuntamento.selectedDate()
        self.data_selezionata = str(dateselected.toPyDate())
        self.label.setText("Data selezionata : " + self.data_selezionata)
        return self.data_selezionata

    def show_selected_orario(self, current):
        if self.list_view_orario.selectedIndexes():
            self.orario_selected = self.orari[current.row()]
            self.label_orario.setText("Fascia oraria selezionata : " + self.orario_selected)
        return self.orario_selected

    def update_ui(self):
        self.list_view_orario_model = QStandardItemModel(self.list_view_orario)
        self.orari = ["9:00-10:00", "10:00-11:00", "11:00-12:00", "12:00-13:00", "13:00-14:00", "14:00-15:00", "15:00-16:00", "16:00-17:00", "17:00-18:00", "18:00-19:00"]
        for fascia in self.orari:
            item = QStandardItem()
            item.setText(fascia)
            item.setEditable(False)
            font = item.font()
            font.setFamily('Georgia')
            font.setPointSize(12)
            item.setFont(font)
            self.list_view_orario_model.appendRow(item)
        self.list_view_orario.setModel(self.list_view_orario_model)