from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon, QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QListView, QVBoxLayout, QGridLayout, QLabel

from magazzino.controller.ControlloreMagazzino import ControlloreMagazzino
from magazzino.view.VistaAggiornaFornitura import VistaAggiornaFornitura
from materiale.view.VistaTampone import VistaTampone
from materiale.view.VistaVaccino import VistaVaccino


class VistaMagazzino(QWidget):

    def __init__(self, parent=None):
        super(VistaMagazzino, self).__init__(parent)
        self.controller = ControlloreMagazzino()

        grid_layout = QGridLayout()
        v_layout_vaccini = QVBoxLayout()
        v_layout_tamponi = QVBoxLayout()

        self.list_view_vaccini = QListView()
        self.list_view_tamponi = QListView()
        self.update_ui()

        font = QFont('Arial Nova Light', 18)

        label_vaccini = QLabel("Presidi sezione vaccini")
        font.setItalic(True)
        label_vaccini.setFont(font)
        v_layout_vaccini.addWidget(label_vaccini)
        v_layout_vaccini.addWidget(self.list_view_vaccini)

        label_tamponi = QLabel("Presidi sezione tamponi")
        font.setItalic(True)
        label_tamponi.setFont(font)
        v_layout_tamponi.addWidget(label_tamponi)
        v_layout_tamponi.addWidget(self.list_view_tamponi)

        buttons_vaccini = QVBoxLayout()
        open_vaccino = QPushButton("Visualizza")
        open_vaccino.clicked.connect(self.show_selected_vaccino)
        buttons_vaccini.addWidget(open_vaccino)
        aggiorna_vaccino = QPushButton("Aggiorna")
        aggiorna_vaccino.clicked.connect(self.aggiorna_selected_vaccino)
        buttons_vaccini.addWidget(aggiorna_vaccino)

        buttons_tamponi = QVBoxLayout()
        open_tampone = QPushButton("Visualizza")
        aggiorna_tampone = QPushButton("Aggiorna")
        open_tampone.clicked.connect(self.show_selected_tampone)
        aggiorna_tampone.clicked.connect(self.aggiorna_selected_tampone)
        buttons_tamponi.addWidget(open_tampone)
        buttons_tamponi.addWidget(aggiorna_tampone)

        grid_layout.addLayout(v_layout_vaccini, 0, 0)
        grid_layout.addLayout(v_layout_tamponi, 0, 1)
        grid_layout.addLayout(buttons_vaccini, 1, 0)
        grid_layout.addLayout(buttons_tamponi, 1, 1)

        self.setLayout(grid_layout)
        self.setFont(QFont('Arial Nova Light'))
        self.setWindowTitle("Lista Presidi")
        self.setWindowIcon(QIcon('appuntamentovaccino/data/CovidFree_Clinica.png'))

        self.setMaximumSize(600, 300)
        self.resize(600, 300)
        self.move(200, 200)

    # Funzione che popola le liste dei presidi presenti nel magazzino
    def update_ui(self):
        self.listview_vaccini_model = QStandardItemModel(self.list_view_vaccini)
        for vaccino in self.controller.get_elenco_vaccini():
            item = QStandardItem()
            item.setText(vaccino.tipologia)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(15)
            item.setFont(font)
            self.listview_vaccini_model.appendRow(item)
        self.list_view_vaccini.setModel(self.listview_vaccini_model)

        self.listview_tamponi_model = QStandardItemModel(self.list_view_tamponi)
        for tampone in self.controller.get_elenco_tamponi():
            item = QStandardItem()
            item.setText(tampone.tipologia)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(15)
            item.setFont(font)
            self.listview_tamponi_model.appendRow(item)
        self.list_view_tamponi.setModel(self.listview_tamponi_model)

    # Funzione che mostra il vaccino selezionato.
    def show_selected_vaccino(self):
         if self.list_view_vaccini.selectedIndexes():
             selected = self.list_view_vaccini.selectedIndexes()[0].row()
             vaccino_selezionato = self.controller.get_presidio_by_index(selected)
             self.vista_vaccino = VistaVaccino(vaccino_selezionato)
             self.vista_vaccino.show()

    # Funzione che mostra il tampone selezionato.
    def show_selected_tampone(self):
         if self.list_view_tamponi.selectedIndexes():
             selected = self.list_view_tamponi.selectedIndexes()[0].row()
             tampone_selezionato = self.controller.get_presidio_by_index(selected+3)
             self.vista_tampone = VistaTampone(tampone_selezionato)
             self.vista_tampone.show()

    # Funzione che mostra la vista che permette l'aggiornamento della quantità del vaccino selezionato.
    def aggiorna_selected_vaccino(self):
         if self.list_view_vaccini.selectedIndexes():
             selected = self.list_view_vaccini.selectedIndexes()[0].row()
             selezionato = self.controller.get_presidio_by_index(selected)
             self.vista_fornitura = VistaAggiornaFornitura(selezionato, self.controller.aggiorna_quantita_by_tipologia,
                                                           self.update_ui)
             self.vista_fornitura.show()

    # Funzione che mostra la vista che permette l'aggiornamento della quantità del tampone selezionato.
    def aggiorna_selected_tampone(self):
         if self.list_view_tamponi.selectedIndexes():
             selected = self.list_view_tamponi.selectedIndexes()[0].row()
             selezionato = self.controller.get_presidio_by_index(selected + 3)
             self.vista_fornitura = VistaAggiornaFornitura(selezionato, self.controller.aggiorna_quantita_by_tipologia,
                                                           self.update_ui)
             self.vista_fornitura.show()

    # Funzione che richiama il metodo del controllore che salva i dati aggiornati.
    def closeEvent(self, event):
        self.controller.save_data()
        event.accept()
