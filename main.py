import sys
import time

from PyQt5 import QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen

from home.view.VistaHome import VistaHome

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(215, 235, 240))
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(255, 255, 255))
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(255, 255, 255))
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(176, 224, 230))
    app.setPalette(palette)

    splash = QSplashScreen(QPixmap('appuntamentovaccino/data/CovidFree_Clinica.png').scaled(507, 605))
    splash.show()
    QTimer.singleShot(3000, splash.close)

    time.sleep(3)

    vista_home = VistaHome()
    vista_home.show()
    sys.exit(app.exec())



