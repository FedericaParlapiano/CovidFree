from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from appuntamentovaccino.view.VistaAppuntamentoVaccino import VistaAppuntamentoVaccino
from calendariovaccini.controller.ControlloreCalendarioVaccini import ControlloreCalendarioVaccini


class VistaListaAppuntamentiVaccini(QWidget):
    def __init__(self, data, callback):

        super(VistaListaAppuntamentiVaccini, self).__init__()
        self.controller = ControlloreCalendarioVaccini()
        self.callback = callback

        h_layout = QHBoxLayout()
        self.list_view_appuntamenti = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view_appuntamenti)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton('Apri')
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle('Lista Appuntamenti Vaccini Giorno: {}'.format(data))

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