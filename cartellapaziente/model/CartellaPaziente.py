from dateutil.relativedelta import relativedelta
from datetime import date, datetime

class CartellaPaziente():
    def __init__(self, nome, cognome, data_di_nascita, cf, indirizzo, telefono, preferenza):
        super(CartellaPaziente, self).__init__()

        self.nome = nome
        self.cognome = cognome
        self.data_di_nascita = data_di_nascita
        self.cf = cf
        self.indirizzo = indirizzo
        #self.patologie = patologie
        self.telefono = telefono
        self.preferenza = preferenza
        #self.categoria = self.assegna_categoria()

    def assegna_categoria(self):

        '''anno_corrente = date.today().year
        anno_di_nascita = datetime.strptime(self.data_di_nascita, '%Y/%m/%d').year

        differenza = anno_corrente - anno_di_nascita

        if differenza >= 80:
            categoria = 'over 80'
        elif differenza >= 70:
            categoria = 'categoria 70-79'
        elif differenza >= 60:
            categoria = 'categoria 60-69'
        elif differenza >= 50:
            categoria = 'categoria 50-59'
        elif differenza >= 40:
            categoria = 'categoria 40-49'
        elif differenza >= 30:
            categoria = 'categoria 30-39'
        else:
            categoria = 'under 30' '''

        return None
