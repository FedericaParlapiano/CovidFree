from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QListView, QVBoxLayout

from magazzino.controller.ControlloreMagazzino import ControlloreMagazzino


class VistaMagazzino(QWidget):

     def __init__(self, parent=None):
        super(VistaMagazzino, self).__init__(parent)

        self.controller = ControlloreMagazzino()


        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.listview_model = QStandardItemModel(self.list_view)


        self.setLayout(h_layout)
        self.setWindowTitle("Magazzino")

        for presidio in self.controller.get_magazzino():
             item = QStandardItem()
             item.setText(presidio.tipologia)
             item.setEditable(False)
             font = item.font()
             font.setPointSize(18)
             item.setFont(font)
             self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()

        open_button = QPushButton("Visualizza")
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle('Lista Presidi')


     def closeEvent(self, event):
        self.controller.save_data()
        event.accept()



     def show_selected_info(self):
          pass




