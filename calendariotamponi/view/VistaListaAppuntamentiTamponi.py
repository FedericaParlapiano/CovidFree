from PyQt5 import QtGui
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QLabel, QGridLayout, QMessageBox

from appuntamentotampone.view.VistaAppuntamentoTampone import VistaAppuntamentoTampone
from calendariotamponi.controller.ControlloreCalendarioTamponi import ControlloreCalendarioTamponi


class VistaListaAppuntamentiTamponi(QWidget):
    def __init__(self, controller, data, callback):

        super(VistaListaAppuntamentiTamponi, self).__init__()
        self.controller = ControlloreCalendarioTamponi()
        self.callback = callback
        self.data = data

        self.elenco_antigenico = []
        self.elenco_molecolare = []
        self.elenco_sierologico = []

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        h_layout.addWidget(self.list_view)

        self.grid_layout = QGridLayout()

        self.list_view_antigenico = QListView()
        self.list_view_molecolare = QListView()
        self.list_view_sierologico = QListView()

        self.update_ui()

        self.get_list("Appuntamenti Antigenico", 0)
        self.get_list("Appuntamenti Molecolare", 1)
        self.get_list("Appuntamenti Sierologico", 2)

        self.grid_layout.addWidget(self.list_view_antigenico, 1, 0)
        self.grid_layout.addWidget(self.list_view_molecolare, 1, 1)
        self.grid_layout.addWidget(self.list_view_sierologico, 1, 2)

        visualizza_antigenico = QPushButton("Visualizza")
        elimina_antigenico = QPushButton("Elimina")
        self.grid_layout.addWidget(visualizza_antigenico, 2, 0)
        self.grid_layout.addWidget(elimina_antigenico, 3, 0)
        visualizza_antigenico.clicked.connect(self.show_selected_info_antigenico)
        elimina_antigenico.clicked.connect(self.elimina_appuntamento_antigenico)

        visualizza_molecolare = QPushButton("Visualizza")
        elimina_molecolare = QPushButton("Elimina")
        self.grid_layout.addWidget(visualizza_molecolare, 2, 1)
        self.grid_layout.addWidget(elimina_molecolare, 3, 1)
        visualizza_molecolare.clicked.connect(self.show_selected_info_molecolare)
        elimina_molecolare.clicked.connect(self.elimina_appuntamento_molecolare)

        visualizza_sierologico = QPushButton("Visualizza")
        elimina_sierologico = QPushButton("Elimina")
        self.grid_layout.addWidget(visualizza_sierologico, 2, 2)
        self.grid_layout.addWidget(elimina_sierologico, 3, 2)
        visualizza_sierologico.clicked.connect(self.show_selected_info_sierologico)
        elimina_sierologico.clicked.connect(self.elimina_appuntamento_sierologico)

        self.setLayout(self.grid_layout)
        self.resize(600, 300)
        self.setWindowTitle('Lista Appuntamenti Tamponi Giorno: {}'.format(self.data))


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

    def show_selected_info_molecolare(self):
        if self.list_view_molecolare.selectedIndexes():
            selected = self.list_view_molecolare.selectedIndexes()[0].row()
            appuntamento_selezionato = self.elenco_molecolare[selected]
            self.vista_tampone = VistaAppuntamentoTampone(appuntamento_selezionato)
            self.vista_tampone.show()
            self.update_ui()

    def show_selected_info_antigenico(self):
        if self.list_view_antigenico.selectedIndexes():
            selected = self.list_view_antigenico.selectedIndexes()[0].row()
            appuntamento_selezionato = self.elenco_antigenico[selected]
            self.vista_tampone = VistaAppuntamentoTampone(appuntamento_selezionato)
            self.vista_tampone.show()
            self.update_ui()

    def show_selected_info_sierologico(self):
        if self.list_view_sierologico.selectedIndexes():
            selected = self.list_view_sierologico.selectedIndexes()[0].row()
            appuntamento_selezionato = self.elenco_sierologico[selected]
            self.vista_tampone = VistaAppuntamentoTampone(appuntamento_selezionato)
            self.vista_tampone.show()
            self.update_ui()

    def update_ui(self):
        self.list_view_antigenico_model = QStandardItemModel(self.list_view_antigenico)
        self.list_view_molecolare_model = QStandardItemModel(self.list_view_molecolare)
        self.list_view_sierologico_model = QStandardItemModel(self.list_view_sierologico)

        for appuntamento in self.controller.get_elenco_appuntamenti():
            item = QStandardItem()
            if appuntamento.data_appuntamento == self.data:
                item.setText(appuntamento.nome + " " + appuntamento.cognome)
                item.setEditable(False)
                font = item.font()
                font.setFamily('Georgia')
                font.setPointSize(12)
                item.setFont(font)
                if appuntamento.is_drive_through:
                    item.setBackground(QtGui.QColor(255,255,153))
                if appuntamento.tipo_tampone == "Antigenico":
                    self.list_view_antigenico_model.appendRow(item)
                    self.elenco_antigenico.append(appuntamento)
                elif appuntamento.tipo_tampone == "Molecolare":
                    self.list_view_molecolare_model.appendRow(item)
                    self.elenco_molecolare.append(appuntamento)
                elif appuntamento.tipo_tampone == "Sierologico":
                    self.list_view_sierologico_model.appendRow(item)
                    self.elenco_sierologico.append(appuntamento)

        self.list_view_antigenico.setModel(self.list_view_antigenico_model)
        self.list_view_molecolare.setModel(self.list_view_molecolare_model)
        self.list_view_sierologico.setModel(self.list_view_sierologico_model)

    def elimina_appuntamento_antigenico(self):
        if self.list_view_antigenico.selectedIndexes():
            selected = self.list_view_antigenico.selectedIndexes()[0].row()
            appuntamento_selezionato = self.elenco_antigenico[selected]

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Sei sicuro di voler eliminare l'appuntamento?")
            msg.setInformativeText("La decisione è irreversibile!")
            msg.setWindowTitle("Conferma eliminazione")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            if msg.exec() == QMessageBox.Ok:
                self.controller.elimina_appuntamento(appuntamento_selezionato)
            self.update_ui()

    def elimina_appuntamento_molecolare(self):
        if self.list_view_molecolare.selectedIndexes():
            selected = self.list_view_molecolare.selectedIndexes()[0].row()
            appuntamento_selezionato = self.elenco_molecolare[selected]

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Sei sicuro di voler eliminare l'appuntamento?")
            msg.setInformativeText("La decisione è irreversibile!")
            msg.setWindowTitle("Conferma eliminazione")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            if msg.exec() == QMessageBox.Ok:
                self.controller.elimina_appuntamento(appuntamento_selezionato)
            self.update_ui()

    def elimina_appuntamento_sierologico(self):
        if self.list_view_sierologico.selectedIndexes():
            selected = self.list_view_sierologico.selectedIndexes()[0].row()
            appuntamento_selezionato = self.elenco_sierologico[selected]

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Sei sicuro di voler eliminare l'appuntamento?")
            msg.setInformativeText("La decisione è irreversibile!")
            msg.setWindowTitle("Conferma eliminazione")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            if msg.exec() == QMessageBox.Ok:
                self.controller.elimina_appuntamento(appuntamento_selezionato)

            self.update_ui()
