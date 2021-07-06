from datetime import date, datetime, timedelta
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QWidget, QListView, QPushButton, QVBoxLayout

from calendariovaccini.controller.ControlloreCalendarioVaccini import ControlloreCalendarioVaccini
from calendariovaccini.view.VistaGreenPass import VistaGreenPass


class VistaListaGreenPass(QWidget):

    def __init__(self, parent = None):
        super(VistaListaGreenPass, self).__init__(parent)
        self.controller = ControlloreCalendarioVaccini()

        self.elenco_green_pass = []

        v_layout = QVBoxLayout()

        self.list_view_elenco_green_pass = QListView()

        self.get_list()

        v_layout.addWidget(self.list_view_elenco_green_pass)

        visualizza = QPushButton("Visualizza")
        v_layout.addWidget(visualizza)
        visualizza.clicked.connect(self.show_selected_green_pass)

        self.setLayout(v_layout)
        self.setFont(QFont('Arial Nova Light', 14))
        self.setWindowTitle('Grenn pass validi al giorno: {}'.format(date.today()))
        self.setWindowIcon(QIcon('appuntamentovaccino/data/CovidFree_Clinica.png'))

        self.setMaximumSize(600, 400)
        self.resize(600, 400)
        self.move(150, 200)

    # Funzione che popola la lista dei green pass attivi al giorno corrente.
    def get_list(self):
        self.list_view_elenco_green_pass_model = QStandardItemModel(self.list_view_elenco_green_pass)

        for appuntamento in self.controller.get_elenco_appuntamenti():
            item = QStandardItem()
            scadenza = datetime.strptime(appuntamento.data_appuntamento, '%d-%m-%Y') + timedelta(days=270)
            scadenza_convertita = date(scadenza.year, scadenza.month, scadenza.day)
            data_appuntamento = datetime.strptime(appuntamento.data_appuntamento, '%d-%m-%Y')
            data_convertita= date(data_appuntamento.year, data_appuntamento.month, data_appuntamento.day)

            if data_convertita < date.today():
                if scadenza_convertita > date.today():
                    if appuntamento.id == "Prima Dose":
                        item.setText(appuntamento.cartella_paziente.nome + " " + appuntamento.cartella_paziente.cognome)
                        item.setEditable(False)
                        font = item.font()
                        font.setFamily('Arial Nova Light')
                        font.setPointSize(13)
                        item.setFont(font)

                        self.list_view_elenco_green_pass_model.appendRow(item)
                        self.elenco_green_pass.append(appuntamento)
        self.list_view_elenco_green_pass.setModel(self.list_view_elenco_green_pass_model)

    # Funzione che mostra il Green Pass selezionato.
    def show_selected_green_pass(self):
        if self.list_view_elenco_green_pass.selectedIndexes():
            selected = self.list_view_elenco_green_pass.selectedIndexes()[0].row()
            appuntamento_selezionato = self.elenco_green_pass[selected]
            self.vista_green_pass = VistaGreenPass(appuntamento_selezionato)
            self.vista_green_pass.show()
