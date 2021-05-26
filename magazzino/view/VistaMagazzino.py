from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton

from magazzino.controller import ControlloreMagazzino


class VistaMagazzino(QWidget):
   def __init__(self, parent=None):
        super(VistaMagazzino, self).__init__(parent)

        self.controller = ControlloreMagazzino

        h_layout = QHBoxLayout()

        button = QPushButton("Visualizza")
        h_layout.addWidget(button)

        self.setLayout(h_layout)
        self.setWindowTitle("Magazzino")


