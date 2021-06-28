import sys
import time

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QPalette, QColor
from PyQt5.QtWidgets import QApplication, QSplashScreen

from home.view.VistaHome import VistaHome

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    splash = QSplashScreen(QPixmap('appuntamentovaccino/data/Girasoli.jpeg').scaled(200, 300))
    splash.show()
    QTimer.singleShot(4000, splash.close)

    time.sleep(4)

    vista_home = VistaHome()
    vista_home.show()
    sys.exit(app.exec())



