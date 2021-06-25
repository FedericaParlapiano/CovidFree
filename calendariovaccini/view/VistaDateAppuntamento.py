from datetime import date, datetime, timedelta
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QListView, QVBoxLayout, QLabel, QPushButton, QMessageBox, QGridLayout
from calendariovaccini.controller.ControlloreCalendarioVaccini import ControlloreCalendarioVaccini

class VistaDateAppuntamento(QWidget):

    def __init__(self):
        super(VistaDateAppuntamento, self).__init__(parent=None)

        self.controller = ControlloreCalendarioVaccini()
        self.appuntamenti = {}
        self.date_da_mostrare = []
        self.orari_disponibili = ["9:00-10:00", "10:00-11:00", "11:00-12:00", "12:00-13:00", "13:00-14:00", "14:00-15:00", "15:00-16:00", "16:00-17:00", "17:00-18:00", "18:00-19:00"]
        self.orari_appuntamenti = {}

        self.v_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()

        self.data_scelta = ""
        self.orario_selezionato = ""

        self.elenco_appuntamenti = self.controller.get_elenco_appuntamenti()

        for appuntamento in self.elenco_appuntamenti:
            if appuntamento.data_appuntamento in self.appuntamenti:
                self.appuntamenti[appuntamento.data_appuntamento] += 1
            else:
                self.appuntamenti[appuntamento.data_appuntamento] = 1

        self.list_view_date = QListView()
        self.list_view_orari = QListView()

        self.label_data = QLabel("Data")
        self.label_orario = QLabel("Fascia Oraria")
        self.grid_layout.addWidget(self.label_data, 0, 0)
        self.grid_layout.addWidget(self.label_orario, 0, 1)

        self.button_data = QPushButton("Seleziona")
        self.button_data.clicked.connect(self.get_data)

        self.button_orario = QPushButton("Seleziona")
        self.button_orario.clicked.connect(self.get_orario)

        self.button_conferma = QPushButton("Conferma")
        self.button_conferma.clicked.connect(self.conferma)

        self.determina_date()
        self.mostra_date()

        self.grid_layout.addWidget(self.list_view_date, 1, 0)
        self.grid_layout.addWidget(self.button_data, 2, 0)
        self.grid_layout.addWidget(self.list_view_orari, 1, 1)
        self.grid_layout.addWidget(self.button_orario, 2, 1)

        self.v_layout.addLayout(self.grid_layout)
        self.v_layout.addWidget(self.button_conferma)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Scelta della data")


    def determina_date(self):
        contatore = 10
        i = 1
        while not contatore == len(self.date_da_mostrare):
            data = datetime.strptime(str(date.today() + timedelta(days=i)), '%Y-%m-%d')
            appuntamento = str(data.strftime('%d-%m-%Y'))
            if appuntamento in self.appuntamenti:
                if self.appuntamenti[appuntamento] < 40:
                    self.date_da_mostrare.append(appuntamento)
            elif appuntamento not in self.appuntamenti:
                self.date_da_mostrare.append(appuntamento)
            i +=1

    def mostra_date(self):
        self.list_view_date_model = QStandardItemModel(self.list_view_date)

        for data in self.date_da_mostrare:
            item = QStandardItem()
            item.setText(data)
            item.setEditable(False)
            font = item.font()
            font.setFamily('Georgia')
            font.setPointSize(12)
            item.setFont(font)
            self.list_view_date_model.appendRow(item)

        self.list_view_date.setModel(self.list_view_date_model)

    def get_data(self):
        self.orari_appuntamenti = {}
        self.orari_disponibili = ["9:00-10:00", "10:00-11:00", "11:00-12:00", "12:00-13:00", "13:00-14:00",
                                  "14:00-15:00", "15:00-16:00", "16:00-17:00", "17:00-18:00", "18:00-19:00"]

        if self.list_view_date.selectedIndexes():
            selected = self.list_view_date.selectedIndexes()[0].row()
            self.data_scelta = self.date_da_mostrare[selected]
            self.label_data.setText("Data selezionata: " + self.data_scelta)

            for appuntamento in self.elenco_appuntamenti:
                if appuntamento.data_appuntamento == self.data_scelta:
                    if appuntamento.fascia_oraria in self.orari_appuntamenti:
                        self.orari_appuntamenti[appuntamento.fascia_oraria] += 1
                    else:
                        self.orari_appuntamenti[appuntamento.fascia_oraria] = 1

            for key in self.orari_appuntamenti:
                if self.orari_appuntamenti[key] > 3:
                    if key in self.orari_disponibili:
                        self.orari_disponibili.remove(key)

            self.mostra_orari()

        else:
            QMessageBox.critical(self, 'Errore', 'Hai dimenticato di inserire una data! Non è possibile procedere!', QMessageBox.Ok, QMessageBox.Ok)

    def mostra_orari(self):
        self.list_view_orari_model = QStandardItemModel(self.list_view_orari)

        for orario in self.orari_disponibili:
                item = QStandardItem()
                item.setText(orario)
                item.setEditable(False)
                font = item.font()
                font.setFamily('Georgia')
                font.setPointSize(12)
                item.setFont(font)
                self.list_view_orari_model.appendRow(item)

        self.list_view_orari.setModel(self.list_view_orari_model)

    def get_orario(self):
        if self.list_view_orari.selectedIndexes():
            selected = self.list_view_orari.selectedIndexes()[0].row()
            self.orario_selezionato = self.orari_disponibili[selected]
            self.label_orario.setText("Fascia oraria selezionata: " + self.orario_selezionato)
        else:
            QMessageBox.critical(self, 'Errore', 'Hai dimenticato di inserire una fascia oraria! Non è possibile procedere!', QMessageBox.Ok, QMessageBox.Ok)

    def conferma(self):
        if self.orario_selezionato != "" and self.data_scelta != "":
            self.registrazione_completa = True
            self.close()
        else:
            QMessageBox.critical(self, 'Errore', 'Selezionare entrambi i parametri!', QMessageBox.Ok, QMessageBox.Ok)