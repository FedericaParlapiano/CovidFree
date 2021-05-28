from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton



class VistaListaAppuntamentiTamponi(QWidget):
    def __init__(self, controller, data, callback):

        super(VistaListaAppuntamentiTamponi, self).__init__()
        self.controller = controller
        self.callback = callback
        self.info = {}

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton('Apri')
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle('Lista Appuntamenti Tamponi Giorno: {}'.format(data))

    def show_selected_info(self):
        pass

    def update_ui(self):
        pass