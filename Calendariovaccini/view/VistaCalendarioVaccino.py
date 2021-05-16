from datetime import datetime
import calendar
from PyQt5.QtWidgets import QWidget, QCalendarWidget, QSizePolicy, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtCore import QDate


class VistaCalendarioVaccini(QWidget):
    global currentYear, currentMonth
    currentMonth = datetime.now().month
    currentYear = datetime.now().year

    def __init__(self, parent=None):
        super(VistaCalendarioVaccini, self).__init__(parent)

        h_layout = QHBoxLayout()
        calendar_layout = QVBoxLayout()
        calendar_layout.addWidget(self.init_calendario())

        buttons_layout = QVBoxLayout()

        visualizza_button = QPushButton("Visualizza")
        # visualizza_button.clicked.connect(self.show_selected_data)
        buttons_layout.addWidget(visualizza_button)

        add_button = QPushButton("Aggiungi Appuntamento")
        # add_button.clicked.connect(self.show_add_appuntamento)
        buttons_layout.addWidget(add_button)

        buttons_layout.addStretch()

        h_layout.addLayout(calendar_layout)
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.setWindowTitle('Calendario Appuntamenti Vaccino')
        self.resize(500,300)


    def init_calendario(self):
        self.calendar = QCalendarWidget(self)
        self.calendar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #self.calendar.setGeometry(200,200,300,200)
        self.calendar.setGridVisible(True)

        self.calendar.setMinimumDate(QDate(currentYear, currentMonth, 1))
        self.calendar.setMaximumDate(QDate(currentYear + 1, currentMonth, calendar.monthrange(currentYear, currentMonth)[1]))
        self.calendar.setSelectedDate(QDate(currentYear, currentMonth, 1))