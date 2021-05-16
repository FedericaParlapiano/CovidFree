from datetime import datetime
import calendar
from PyQt5.QtWidgets import QWidget, QCalendarWidget, QSizePolicy, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtCore import QDate


class VistaCalendarioVaccini(QWidget):

    def __init__(self, parent=None):

        super(VistaCalendarioVaccini, self).__init__(parent)

        calendario = QCalendarWidget(self)
        calendario.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        calendario.setGeometry(200,200,300,200)
        calendario.setGridVisible(True)

        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        calendario.setMinimumDate(QDate(currentYear, currentMonth, 1))
        calendario.setMaximumDate(QDate(currentYear + 1, currentMonth, calendar.monthrange(currentYear, currentMonth)[1]))
        calendario.setSelectedDate(QDate(currentYear, currentMonth, 1))

        h_layout = QHBoxLayout()
        calendar_layout = QVBoxLayout()
        calendar_layout.addWidget(calendario)

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


