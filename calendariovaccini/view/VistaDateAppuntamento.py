from datetime import date, datetime, timedelta

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QListView, QVBoxLayout

from calendariovaccini.controller.ControlloreCalendarioVaccini import ControlloreCalendarioVaccini


class VistaDateAppuntamento(QWidget):

    def __init__(self):
        super(VistaDateAppuntamento, self).__init__(parent=None)
        self.controller = ControlloreCalendarioVaccini()
        self.appuntamenti = {}
        self.date_da_mostrare = []

        for appuntamento in self.controller.get_elenco_appuntamenti():
            if appuntamento.data_appuntamento in self.appuntamenti:
                self.appuntamenti[appuntamento.data_appuntamento] += 1
            else:
                self.appuntamenti[appuntamento.data_appuntamento] = 1

        self.list_view_date = QListView()
        self.determina_date()
        self.mostra_date()

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.list_view_date)
        self.setLayout(self.v_layout)

        if self.list_view_date.selectedIndexes():
            self.close()


    def determina_date(self):
        contatore = 3
        i = 1
        while not contatore == len(self.date_da_mostrare):
            data = datetime.strptime(str(date.today() + timedelta(days=i)), '%Y-%m-%d')
            appuntamento = str(data.strftime('%d-%m-%Y'))
            if appuntamento in self.appuntamenti:
                if self.appuntamenti[appuntamento] < 40:
                    self.date_da_mostrare.append(appuntamento)
            elif appuntamento not in self.appuntamenti:
                self.date_da_mostrare.append(appuntamento)
            i +=1

    def mostra_date(self):
        self.list_view_date_model = QStandardItemModel(self.list_view_date)
        for data in self.date_da_mostrare:
            item = QStandardItem()
            item.setText(data)
            item.setEditable(False)
            font = item.font()
            font.setFamily('Georgia')
            font.setPointSize(12)
            item.setFont(font)
            self.list_view_date_model.appendRow(item)
        self.list_view_date.setModel(self.list_view_date_model)