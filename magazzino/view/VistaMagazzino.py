from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QListView, QVBoxLayout, QGridLayout, QLabel, QSizePolicy

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

        label_vaccini = QLabel("Presidi sezione vaccini")
        font_vaccini = label_vaccini.font()
        font_vaccini.setFamily('Georgia')
        font_vaccini.setPointSize(15)
        font_vaccini.setItalic(True)
        label_vaccini.setFont(font_vaccini)
        v_layout_vaccini.addWidget(label_vaccini)
        v_layout_vaccini.addWidget(self.list_view_vaccini)

        label_tamponi = QLabel("Presidi sezione tamponi")
        font_tamponi = label_vaccini.font()
        font_tamponi.setFamily('Georgia')
        font_tamponi.setPointSize(15)
        font_tamponi.setItalic(True)
        label_tamponi.setFont(font_tamponi)
        v_layout_tamponi.addWidget(label_tamponi)
        v_layout_tamponi.addWidget(self.list_view_tamponi)

        buttons_vaccini = QVBoxLayout()
        open_vaccino = QPushButton("Visualizza")
        open_vaccino.clicked.connect(self.show_selected_vaccino)
        buttons_vaccini.addWidget(open_vaccino)
        aggiorna_vaccino = QPushButton("Aggiorna")
        aggiorna_vaccino.clicked.connect(self.aggiorna_selected_materiale)
        buttons_vaccini.addWidget(aggiorna_vaccino)

        buttons_tamponi = QVBoxLayout()
        open_tampone = QPushButton("Visualizza")
        aggiorna_tampone = QPushButton("Aggiorna")
        open_tampone.clicked.connect(self.show_selected_tampone)
        aggiorna_tampone.clicked.connect(self.aggiorna_selected_materiale)
        buttons_tamponi.addWidget(open_tampone)
        buttons_tamponi.addWidget(aggiorna_tampone)

        grid_layout.addLayout(v_layout_vaccini, 0, 0)
        grid_layout.addLayout(v_layout_tamponi, 0, 1)
        grid_layout.addLayout(buttons_vaccini, 1, 0)
        grid_layout.addLayout(buttons_tamponi, 1, 1)

        self.setLayout(grid_layout)
        self.resize(600, 300)
        self.setWindowTitle("Lista Presidi")

    def update_ui(self):
        self.listview_vaccini_model = QStandardItemModel(self.list_view_vaccini)
        for vaccino in self.controller.get_vaccini():
            item = QStandardItem()
            item.setText(vaccino.tipologia)
            item.setEditable(False)
            font = item.font()
            font.setFamily('Georgia')
            font.setPointSize(12)
            item.setFont(font)
            self.listview_vaccini_model.appendRow(item)
        self.list_view_vaccini.setModel(self.listview_vaccini_model)

        self.listview_tamponi_model = QStandardItemModel(self.list_view_tamponi)
        for tampone in self.controller.get_tamponi():
            item = QStandardItem()
            item.setText(tampone.tipologia)
            item.setEditable(False)
            font = item.font()
            font.setFamily('Georgia')
            font.setPointSize(12)
            item.setFont(font)
            self.listview_tamponi_model.appendRow(item)
        self.list_view_tamponi.setModel(self.listview_tamponi_model)

    def show_selected_vaccino(self):
         if self.list_view_vaccini.selectedIndexes():
             selected = self.list_view_vaccini.selectedIndexes()[0].row()
             vaccino_selezionato = self.controller.get_presidio_by_index(selected)
             self.vista_vaccino = VistaVaccino(vaccino_selezionato)
             self.vista_vaccino.show()

    def show_selected_tampone(self):
         if self.list_view_tamponi.selectedIndexes():
             selected = self.list_view_tamponi.selectedIndexes()[0].row()
             tampone_selezionato = self.controller.get_presidio_by_index(selected+3)
             self.vista_tampone = VistaTampone(tampone_selezionato)
             self.vista_tampone.show()

    def aggiorna_selected_materiale(self):
         if self.list_view_vaccini.selectedIndexes():
             selected = self.list_view_vaccini.selectedIndexes()[0].row()
             selezionato = self.controller.get_presidio_by_index(selected)
         elif self.list_view_tamponi.selectedIndexes():
             selected = self.list_view_tamponi.selectedIndexes()[0].row()
             selezionato = self.controller.get_presidio_by_index(selected + 3)

         self.vista_fornitura = VistaAggiornaFornitura(selezionato, self.controller.aggiorna_quantita_by_tipologia, self.update_ui)
         self.vista_fornitura.show()

    def closeEvent(self, event):
        self.controller.save_data()
        event.accept()