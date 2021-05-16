import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication

from Home.view.VistaHome import VistaHome

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    vista_home = VistaHome()
    vista_home.show()
    sys.exit(app.exec())
