from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QListView, QVBoxLayout, QGridLayout, QLabel, QSizePolicy

from magazzino.controller.ControlloreMagazzino import ControlloreMagazzino


class VistaMagazzino(QWidget):

     def __init__(self, parent=None):

        super(VistaMagazzino, self).__init__(parent)

        self.controller = ControlloreMagazzino()

        grid_layout = QGridLayout()
        v_layout_vaccini = QVBoxLayout()
        v_layout_tamponi = QVBoxLayout()

        self.list_view_vaccini = QListView()
        self.listview_vaccini_model = QStandardItemModel(self.list_view_vaccini)
        self.list_view_tamponi = QListView()
        self.listview_tamponi_model = QStandardItemModel(self.list_view_tamponi)

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

        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Visualizza")
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)
        buttons_layout.addStretch()

        grid_layout.addLayout(v_layout_vaccini, 0, 0)
        grid_layout.addLayout(v_layout_tamponi, 0, 1)
        grid_layout.addLayout(buttons_layout, 0, 2)

        self.setLayout(grid_layout)
        self.resize(600, 300)
        self.setWindowTitle("Lista Presidi")


     def closeEvent(self, event):
        self.controller.save_data()
        event.accept()



     def show_selected_info(self):
          pass




