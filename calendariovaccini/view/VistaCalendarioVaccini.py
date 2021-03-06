from datetime import datetime
import calendar
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QCalendarWidget, QSizePolicy, QVBoxLayout, QPushButton, QLabel, \
    QGridLayout, QDesktopWidget
from PyQt5.QtCore import QDate, Qt

from calendariovaccini.view.VistaListaGreenPass import VistaListaGreenPass
from calendariovaccini.view.VistaRicercaAppuntamentoVaccino import VistaRicercaAppuntamentoVaccino
from calendariovaccini.controller.ControlloreCalendarioVaccini import ControlloreCalendarioVaccini
from calendariovaccini.view.VistaInserisciAppuntamentoVaccino import VistaInserisciAppuntamentoVaccino
from calendariovaccini.view.VistaListaAppuntamentiVaccini import VistaListaAppuntamentiVaccini


class VistaCalendarioVaccini(QWidget):

    def __init__(self, parent=None):
        super(VistaCalendarioVaccini, self).__init__(parent)

        self.controller = ControlloreCalendarioVaccini()
        self.calendario_vaccini = self.init_calendario()

        grid_layout = QGridLayout()
        calendar_layout = QVBoxLayout()
        calendar_layout.addWidget(self.calendario_vaccini)

        self.calendario_vaccini.selectionChanged.connect(self.calendar_date)
        self.label = QLabel('')
        calendar_layout.addWidget(self.label)

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(self.get_generic_button("Visualizza", self.show_selected_data))
        buttons_layout.addWidget(self.get_generic_button("Aggiungi Appuntamento", self.show_add_appuntamento))
        buttons_layout.addWidget(self.get_generic_button("Ricerca Appuntamento", self.show_ricerca_appuntamento))
        buttons_layout.addWidget(self.get_generic_button("Green pass", self.show_green_pass_list))

        grid_layout.addLayout(calendar_layout, 0, 0)
        grid_layout.addLayout(buttons_layout, 0, 1, alignment=Qt.AlignBottom)

        self.setLayout(grid_layout)
        self.setWindowTitle("Calendario Appuntamenti Vaccini")
        self.setWindowIcon(QIcon('appuntamentovaccino/data/CovidFree_Clinica.png'))

        self.setMaximumSize(1000, 650)
        self.resize(910, 650)
        self.move(0, 0)

    # Funzione che inizializza il calendario dell'interfaccia grafica.
    def init_calendario(self):
        calendario = QCalendarWidget(self)
        currentMonth = datetime.now().month
        currentYear = datetime.now().year

        calendario.setMinimumDate(QDate(currentYear, currentMonth, 1))
        calendario.setMaximumDate(QDate(currentYear + 1, currentMonth, calendar.monthrange(currentYear, currentMonth)[1]))
        calendario.setSelectedDate(QDate(currentYear, currentMonth, 1))

        calendario.setFont(QFont('Arial Nova Light', 18))
        calendario.setStyleSheet('background-color: lightblue')
        calendario.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        calendario.setGeometry(200, 200, 300, 200)
        calendario.setGridVisible(True)
        return calendario

    # Funzione che viene richiamata per creare un bottone.
    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setFont(QFont('Arial Nova Light', 15))
        if titolo == "Green pass":
            button.setStyleSheet("background-color: rgb(145, 234, 152)")
        button.clicked.connect(on_click)
        return button

    # Funzione che mostra la lista degli appuntamenti associati alla data selezionata.
    def show_selected_data(self):
        self.vista_visualizza_appuntamenti = VistaListaAppuntamentiVaccini(self.calendar_date(), self.controller)
        self.vista_visualizza_appuntamenti.show()

    # Funzione che mostra la vista  per l'inserimento dei dati, da parte dell'utente, per fissare un appuntamento.
    def show_add_appuntamento(self):
        self.vista_inserisci_appuntamento = VistaInserisciAppuntamentoVaccino(self.controller)
        self.vista_inserisci_appuntamento.show()

    # Funzione che mostra la vista per la ricerca di un appuntamento.
    def show_ricerca_appuntamento(self):
        self.vista_ricerca_appuntamento = VistaRicercaAppuntamentoVaccino()
        self.vista_ricerca_appuntamento.show()

    # Funzione che mostra la lista dei Green Pass disponibili al giorno corrente.
    def show_green_pass_list(self):
        self.vista_lista_green_pass = VistaListaGreenPass()
        self.vista_lista_green_pass.show()

    # Funzione che restituisce la data selezionata.
    def calendar_date(self):
        dateselected = self.calendario_vaccini.selectedDate()
        data_selezionata = str(dateselected.toPyDate())
        self.setFont(QFont('Arial Nova Light', 12))
        self.label.setText("Data selezionata : " + data_selezionata)
        return data_selezionata