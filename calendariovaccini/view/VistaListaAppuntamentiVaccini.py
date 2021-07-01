from datetime import datetime, date

from PyQt5 import QtGui
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QIcon, QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QGridLayout, QLabel, QMessageBox

from appuntamentovaccino.view.VistaAppuntamentoVaccino import VistaAppuntamentoVaccino
from calendariovaccini.view.VistaModificaAppuntamentoVaccino import VistaModificaAppuntamentoVaccino


class VistaListaAppuntamentiVaccini(QWidget):

    def __init__(self, data, controller, parent = None):
        super(VistaListaAppuntamentiVaccini, self).__init__(parent)
        self.controller = controller

        appuntamento = datetime.strptime(data, '%Y-%m-%d')
        d = str(appuntamento.strftime('%d-%m-%Y'))
        self.data = d

        self.elenco_astrazeneca = []
        self.elenco_moderna = []
        self.elenco_pfizer = []

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        h_layout.addWidget(self.list_view)

        self.grid_layout = QGridLayout()

        self.list_view_astrazeneca = QListView()
        self.list_view_moderna = QListView()
        self.list_view_pfizer = QListView()

        self.update_ui()

        self.get_list("Appuntamenti Astrazeneca", 0)
        self.get_list("Appuntamenti Moderna", 1)
        self.get_list("Appuntamenti Pfizer", 2)

        self.grid_layout.addWidget(self.list_view_astrazeneca, 1, 0)
        self.grid_layout.addWidget(self.list_view_moderna, 1, 1)
        self.grid_layout.addWidget(self.list_view_pfizer, 1, 2)

        visualizza_astrazeneca = QPushButton("Visualizza")
        elimina_astrazeneca = QPushButton("Elimina")
        modifica_astrazeneca = QPushButton("Modifica")
        self.grid_layout.addWidget(visualizza_astrazeneca, 2, 0)
        self.grid_layout.addWidget(elimina_astrazeneca, 3, 0)
        self.grid_layout.addWidget(modifica_astrazeneca, 4, 0)
        visualizza_astrazeneca.clicked.connect(self.show_selected_info_astrazeneca)
        elimina_astrazeneca.clicked.connect(self.elimina_appuntamento_astrazeneca)
        modifica_astrazeneca.clicked.connect(self.modifica_appuntamento_astrazeneca)

        visualizza_moderna = QPushButton("Visualizza")
        elimina_moderna = QPushButton("Elimina")
        modifica_moderna = QPushButton("Modifica")
        self.grid_layout.addWidget(visualizza_moderna, 2, 1)
        self.grid_layout.addWidget(elimina_moderna, 3, 1)
        self.grid_layout.addWidget(modifica_moderna, 4, 1)
        visualizza_moderna.clicked.connect(self.show_selected_info_moderna)
        elimina_moderna.clicked.connect(self.elimina_appuntamento_moderna)
        modifica_moderna.clicked.connect(self.modifica_appuntamento_moderna)

        visualizza_pfizer = QPushButton("Visualizza")
        elimina_pfizer = QPushButton("Elimina")
        modifica_pfizer = QPushButton("Modifica")
        self.grid_layout.addWidget(visualizza_pfizer, 2, 2)
        self.grid_layout.addWidget(elimina_pfizer, 3, 2)
        self.grid_layout.addWidget(modifica_pfizer, 4, 2)
        visualizza_pfizer.clicked.connect(self.show_selected_info_pfizer)
        elimina_pfizer.clicked.connect(self.elimina_appuntamento_pfizer)
        modifica_pfizer.clicked.connect(self.modifica_appuntamento_pfizer)

        self.setFont(QFont('Arial Nova Light', 14))

        self.setLayout(self.grid_layout)
        self.setWindowTitle('Lista Appuntamenti Vaccini Giorno: {}'.format(self.data))
        self.setWindowIcon(QIcon('appuntamentovaccino/data/CovidFree_Clinica.png'))

        self.setMaximumSize(910, 400)
        self.resize(910, 400)
        self.move(0,0)

    def get_list(self, tipologia, colonna):

        v_layout_tipologia = QVBoxLayout()
        label_tipologia = QLabel(tipologia)
        font_tipologia = label_tipologia.font()
        font_tipologia.setFamily('Georgia')
        font_tipologia.setPointSize(15)
        font_tipologia.setItalic(True)
        label_tipologia.setFont(font_tipologia)
        v_layout_tipologia.addWidget(label_tipologia)

        self.grid_layout.addLayout(v_layout_tipologia, 0, colonna)

    def show_selected_info_astrazeneca(self):
        if self.list_view_astrazeneca.selectedIndexes():
            selected = self.list_view_astrazeneca.selectedIndexes()[0].row()
            appuntamento_selezionato = self.elenco_astrazeneca[selected]
            self.vista_vaccino = VistaAppuntamentoVaccino(appuntamento_selezionato)
            self.vista_vaccino.show()
            self.update_ui()

    def show_selected_info_moderna(self):
        if self.list_view_moderna.selectedIndexes():
            selected = self.list_view_moderna.selectedIndexes()[0].row()
            appuntamento_selezionato = self.elenco_moderna[selected]
            self.vista_vaccino = VistaAppuntamentoVaccino(appuntamento_selezionato)
            self.vista_vaccino.show()
            self.update_ui()

    def show_selected_info_pfizer(self):
        if self.list_view_pfizer.selectedIndexes():
            selected = self.list_view_pfizer.selectedIndexes()[0].row()
            appuntamento_selezionato = self.elenco_pfizer[selected]
            self.vista_vaccino = VistaAppuntamentoVaccino(appuntamento_selezionato)
            self.vista_vaccino.show()
            self.update_ui()

    def update_ui(self):
        self.list_view_astrazeneca_model = QStandardItemModel(self.list_view_astrazeneca)
        self.list_view_moderna_model = QStandardItemModel(self.list_view_moderna)
        self.list_view_pfizer_model = QStandardItemModel(self.list_view_pfizer)

        for appuntamento in self.controller.get_elenco_appuntamenti():
            item = QStandardItem()
            if appuntamento.data_appuntamento == self.data:
                item.setText(appuntamento.cartella_paziente.nome + " " + appuntamento.cartella_paziente.cognome)
                item.setEditable(False)
                font = item.font()
                font.setFamily('Arial Nova Light')
                font.setPointSize(15)
                item.setFont(font)

                if appuntamento.is_a_domicilio:
                    item.setBackground(QtGui.QColor(255,255,153))

                if appuntamento.id == 'Seconda Dose':
                    item.setBackground(QtGui.QColor(255, 200, 153))

                if appuntamento.vaccino == "Astrazeneca":
                    self.list_view_astrazeneca_model.appendRow(item)
                    self.elenco_astrazeneca.append(appuntamento)
                elif appuntamento.vaccino == "Moderna":
                    self.list_view_moderna_model.appendRow(item)
                    self.elenco_moderna.append(appuntamento)
                elif appuntamento.vaccino == "Pfizer":
                    self.list_view_pfizer_model.appendRow(item)
                    self.elenco_pfizer.append(appuntamento)

        self.list_view_astrazeneca.setModel(self.list_view_astrazeneca_model)
        self.list_view_moderna.setModel(self.list_view_moderna_model)
        self.list_view_pfizer.setModel(self.list_view_pfizer_model)

    def elimina_appuntamento_astrazeneca(self):
        if self.list_view_astrazeneca.selectedIndexes():
            selected = self.list_view_astrazeneca.selectedIndexes()[0].row()
            appuntamento_selezionato = self.elenco_astrazeneca[selected]

            data_appuntamento_selezionato = datetime.strptime(appuntamento_selezionato.data_appuntamento, '%d-%m-%Y')
            selezionato = str(data_appuntamento_selezionato.strftime('%Y-%m-%d'))
            if selezionato < str(date.today()):
                QMessageBox.critical(self, 'Errore', 'Non è possibile eliminare appuntamenti passati',
                                     QMessageBox.Ok, QMessageBox.Ok)
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Sei sicuro di voler eliminare l'appuntamento?")
                msg.setWindowIcon(QIcon('appuntamentovaccino/data/CovidFree_Clinica.png'))
                msg.setInformativeText("La decisione è irreversibile!")
                msg.setDetailedText("N.B. Se l'appuntamento da eliminare è assocato ad un secondo appuntamento, anche questo verrà rimosso.")
                msg.setWindowTitle("Conferma eliminazione")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msg.move(250,100)

                if msg.exec() == QMessageBox.Ok:
                    self.controller.lettura_magazzino()
                    self.controller.aggiorna_magazzino(appuntamento_selezionato.vaccino)
                    self.controller.elimina_appuntamento(appuntamento_selezionato)
                    self.elenco_astrazeneca.remove(appuntamento_selezionato)

                    if appuntamento_selezionato.id == 'Prima Dose':
                        seconda_dose = self.controller.get_appuntamento(appuntamento_selezionato.cartella_paziente.nome,
                                                                        appuntamento_selezionato.cartella_paziente.cognome,
                                                                        'Seconda Dose')
                        if seconda_dose is not None:
                            self.controller.lettura_magazzino()
                            self.controller.aggiorna_magazzino(seconda_dose.vaccino)
                            self.controller.elimina_appuntamento(seconda_dose)

                self.update_ui()

    def elimina_appuntamento_moderna(self):
        if self.list_view_moderna.selectedIndexes():
            selected = self.list_view_moderna.selectedIndexes()[0].row()
            appuntamento_selezionato = self.elenco_moderna[selected]

            data_appuntamento_selezionato = datetime.strptime(appuntamento_selezionato.data_appuntamento, '%d-%m-%Y')
            selezionato = str(data_appuntamento_selezionato.strftime('%Y-%m-%d'))
            if selezionato < str(date.today()):
                QMessageBox.critical(self, 'Errore', 'Non è possibile eliminare appuntamenti passati',
                                     QMessageBox.Ok, QMessageBox.Ok)
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Sei sicuro di voler eliminare l'appuntamento?")
                msg.setInformativeText("La decisione è irreversibile!")
                msg.setWindowTitle("Conferma eliminazione")
                msg.setDetailedText("N.B. Se l'appuntamento da eliminare è assocato ad un secondo appuntamento, anche questo verrà rimosso.")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msg.move(250,100)

                if msg.exec() == QMessageBox.Ok:
                    self.controller.lettura_magazzino()
                    self.controller.aggiorna_magazzino(appuntamento_selezionato.vaccino)
                    self.controller.elimina_appuntamento(appuntamento_selezionato)
                    self.elenco_moderna.remove(appuntamento_selezionato)

                    if appuntamento_selezionato.id == 'Prima Dose':
                        seconda_dose = self.controller.get_appuntamento(appuntamento_selezionato.cartella_paziente.nome,
                                                                        appuntamento_selezionato.cartella_paziente.cognome,
                                                                        'Seconda Dose')
                        if seconda_dose is not None:
                            self.controller.lettura_magazzino()
                            self.controller.aggiorna_magazzino(seconda_dose.vaccino)
                            self.controller.elimina_appuntamento(seconda_dose)

                self.update_ui()

    def elimina_appuntamento_pfizer(self):
        if self.list_view_pfizer.selectedIndexes():
            selected = self.list_view_pfizer.selectedIndexes()[0].row()
            appuntamento_selezionato = self.elenco_pfizer[selected]

            data_appuntamento_selezionato = datetime.strptime(appuntamento_selezionato.data_appuntamento, '%d-%m-%Y')
            selezionato = str(data_appuntamento_selezionato.strftime('%Y-%m-%d'))
            if selezionato < str(date.today()):
                QMessageBox.critical(self, 'Errore', 'Non è possibile eliminare appuntamenti passati',
                                     QMessageBox.Ok, QMessageBox.Ok)
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Sei sicuro di voler eliminare l'appuntamento?")
                msg.setInformativeText("La decisione è irreversibile!")
                msg.setWindowTitle("Conferma eliminazione")
                msg.setDetailedText("N.B. Se l'appuntamento da eliminare è assocato ad un secondo appuntamento, anche questo verrà rimosso.")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msg.move(250, 100)

                if msg.exec() == QMessageBox.Ok:
                    self.controller.lettura_magazzino()
                    self.controller.aggiorna_magazzino(appuntamento_selezionato.vaccino)
                    self.controller.elimina_appuntamento(appuntamento_selezionato)
                    self.elenco_pfizer.remove(appuntamento_selezionato)

                    if appuntamento_selezionato.id == 'Prima Dose':
                        seconda_dose = self.controller.get_appuntamento(appuntamento_selezionato.cartella_paziente.nome,
                                                                        appuntamento_selezionato.cartella_paziente.cognome,
                                                                        'Seconda Dose')
                        if seconda_dose is not None:
                            self.controller.lettura_magazzino()
                            self.controller.aggiorna_magazzino(seconda_dose.vaccino)
                            self.controller.elimina_appuntamento(seconda_dose)

                self.update_ui()

    def modifica_appuntamento_astrazeneca(self):
        if self.list_view_astrazeneca.selectedIndexes():
            selected = self.list_view_astrazeneca.selectedIndexes()[0].row()
            appuntamento_selezionato = self.elenco_astrazeneca[selected]
            self.vista_modifica = VistaModificaAppuntamentoVaccino(appuntamento_selezionato, self.controller)
            self.vista_modifica.show()
            self.close()

    def modifica_appuntamento_moderna(self):
        if self.list_view_moderna.selectedIndexes():
            selected = self.list_view_moderna.selectedIndexes()[0].row()
            appuntamento_selezionato = self.elenco_moderna[selected]
            self.vista_modifica = VistaModificaAppuntamentoVaccino(appuntamento_selezionato, self.controller)
            self.vista_modifica.show()
            self.close()

    def modifica_appuntamento_pfizer(self):
        if self.list_view_pfizer.selectedIndexes():
            selected = self.list_view_pfizer.selectedIndexes()[0].row()
            appuntamento_selezionato = self.elenco_pfizer[selected]
            self.vista_modifica = VistaModificaAppuntamentoVaccino(appuntamento_selezionato,self.controller)
            self.vista_modifica.show()
            self.close()