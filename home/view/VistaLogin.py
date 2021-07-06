from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from home.view.VistaHome import VistaHome

class VistaLogin(QWidget):

    def __init__(self, parent = None):
        super(VistaLogin, self).__init__(parent)


        layout = QGridLayout()
        label1 = QLabel('User Name')
        self.user_name = QLineEdit()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.user_name, 0, 1)

        label2 = QLabel('Password')
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.password, 1, 1)

        button_login = QPushButton('Accedi')
        button_login.clicked.connect(self.controllo_accesso)
        layout.addWidget(button_login, 2, 0, 2, 2, alignment=Qt.AlignBottom)

        self.setLayout(layout)
        self.setWindowTitle('Login')

        self.setFont(QFont('Arial Nova Light', 14))
        self.setWindowIcon(QIcon('appuntamentovaccino/data/CovidFree_Clinica.png'))
        self.resize(500, 170)
        self.move(50, 100)

    # Funzione che controlla il corretto inserimento delle credenziali di accesso.
    def controllo_accesso(self):
        if self.user_name.text() == 'Clinica CovidFree' and self.password.text() == 'CovidFree':
            self.vista_home = VistaHome()
            self.vista_home.show()
            self.close()
        else:
            QMessageBox.critical(self, 'Accesso Negato', 'Le credenziali inserite sono errate', QMessageBox.Ok, QMessageBox.Ok)
