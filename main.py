import sys
import time

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QPalette, QColor
from PyQt5.QtWidgets import QApplication, QSplashScreen

from home.view.VistaHome import VistaHome

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    splash = QSplashScreen(QPixmap('appuntamentovaccino/data/CovidFree_Clinica.png').scaled(507, 605))
    splash.show()
    QTimer.singleShot(3000, splash.close)

    time.sleep(3)

    vista_home = VistaHome()
    vista_home.show()
    sys.exit(app.exec())



