import sys
import time

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QPalette, QColor
from PyQt5.QtWidgets import QApplication, QSplashScreen

from home.view.VistaHome import VistaHome

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(215, 235, 240))
    #palette.setColor(QtGui.QPalette.Window, QtGui.QColor(219, 255, 253))
    #palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(255, 255, 255))
    #palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(219, 255, 253))
    #palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    #palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    #palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(255, 255, 255))
    #palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    #palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)

    #palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142, 45, 197).lighter())
    #palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(150, 150, 197).lighter())
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(176, 224, 230))
    #palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    app.setPalette(palette)

    splash = QSplashScreen(QPixmap('appuntamentovaccino/data/CovidFree_Clinica.png').scaled(507, 605))
    splash.show()
    QTimer.singleShot(3000, splash.close)

    time.sleep(3)

    vista_home = VistaHome()
    vista_home.show()
    sys.exit(app.exec())



