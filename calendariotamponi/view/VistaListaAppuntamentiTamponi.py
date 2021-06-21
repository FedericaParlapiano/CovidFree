from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QLabel, QGridLayout


class VistaListaAppuntamentiTamponi(QWidget):
    def __init__(self, controller, data, callback):

        super(VistaListaAppuntamentiTamponi, self).__init__()
        self.controller = controller
        self.callback = callback
        self.info = {}

        self.update_ui()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        h_layout.addWidget(self.list_view)

        self.grid_layout = QGridLayout()

        self.list_view_antigenico = QListView()
        self.list_view_molecolare = QListView()
        self.list_view_sierologico = QListView()

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

        visualizza_molecolare = QPushButton("Visualizza")
        elimina_molecolare = QPushButton("Elimina")
        self.grid_layout.addWidget(visualizza_molecolare, 2, 1)
        self.grid_layout.addWidget(elimina_molecolare, 3, 1)

        visualizza_sierologico = QPushButton("Visualizza")
        elimina_sierologico = QPushButton("Elimina")
        self.grid_layout.addWidget(visualizza_sierologico, 2, 2)
        self.grid_layout.addWidget(elimina_sierologico, 3, 2)

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
        pass

    def update_ui(self):
        pass