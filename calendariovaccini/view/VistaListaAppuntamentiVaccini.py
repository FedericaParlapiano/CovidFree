from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QGridLayout, QLabel

from appuntamentovaccino.view.VistaAppuntamentoVaccino import VistaAppuntamentoVaccino
from calendariovaccini.controller.ControlloreCalendarioVaccini import ControlloreCalendarioVaccini


class VistaListaAppuntamentiVaccini(QWidget):
    def __init__(self, data, callback):

        super(VistaListaAppuntamentiVaccini, self).__init__()
        self.callback = callback
        self.info = {}

        #self.update_ui()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        h_layout.addWidget(self.list_view)

        self.list_view_appuntamenti = QListView()

        self.grid_layout = QGridLayout()

        self.list_view_astrazeneca = QListView()
        self.list_view_moderna = QListView()
        self.list_view_pfizer = QListView()

        self.get_list("Appuntamenti Astrazeneca", 0)
        self.get_list("Appuntamenti Moderna", 1)
        self.get_list("Appuntamenti Pfizer", 2)

        self.grid_layout.addWidget(self.list_view_astrazeneca, 1, 0)
        self.grid_layout.addWidget(self.list_view_moderna, 1, 1)
        self.grid_layout.addWidget(self.list_view_pfizer, 1, 2)

        visualizza_astrazeneca = QPushButton("Visualizza")
        elimina_astrazeneca = QPushButton("Elimina")
        self.grid_layout.addWidget(visualizza_astrazeneca, 2, 0)
        self.grid_layout.addWidget(elimina_astrazeneca, 3, 0)

        visualizza_moderna = QPushButton("Visualizza")
        elimina_moderna = QPushButton("Elimina")
        self.grid_layout.addWidget(visualizza_moderna, 2, 1)
        self.grid_layout.addWidget(elimina_moderna, 3, 1)

        visualizza_pfizer = QPushButton("Visualizza")
        elimina_pfizer = QPushButton("Elimina")
        self.grid_layout.addWidget(visualizza_pfizer, 2, 2)
        self.grid_layout.addWidget(elimina_pfizer, 3, 2)

        self.setLayout(self.grid_layout)
        self.resize(600, 300)
        self.setWindowTitle('Lista Appuntamenti Tamponi Giorno: {}'.format(data))

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

    def show_selected_info(self):
        if self.list_view_appuntamenti.selectedIndexes():
            selected = self.list_view_appuntamenti.selectedIndexes()[0].row()
            appuntamento_selezionato = self.controller.get_presidio_by_index(selected)
            self.vista_appuntamento = VistaAppuntamentoVaccino(appuntamento_selezionato, self.update_ui, self.controller.elimina_by_id)
            self.vista_vaccino.show()

    def update_ui(self):
        self.listview_appuntamenti_model = QStandardItemModel(self.list_view_appuntamenti)
        if self.controller.get_elenco_appuntamenti():
            for appuntamento in self.controller.get_elenco_appuntamenti():item = QStandardItem()
            item.setText(appuntamento.cartella_paziente.nome + " " + appuntamento.cartella_paziente.cognome)
            item.setEditable(False)
            font = item.font()
            font.setFamily('Georgia')
            font.setPointSize(12)
            item.setFont(font)
            self.listview_appuntamenti_model.appendRow(item)
        self.list_view_appuntamenti.setModel(self.listview_appuntamenti_model)