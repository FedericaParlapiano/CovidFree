from datetime import date, datetime

class CartellaPaziente():
    def __init__(self, nome, cognome, data_di_nascita, cf, indirizzo, telefono, categoria, preferenza, anamnesi):
        super(CartellaPaziente, self).__init__()

        self.nome = nome
        self.cognome = cognome
        self.data_di_nascita = data_di_nascita
        self.cf = cf
        self.indirizzo = indirizzo
        self.telefono = telefono
        self.preferenza = preferenza
        self.anamnesi = anamnesi
        if categoria == ' ':
            self.categoria = self.assegna_categoria()
        else:
            self.categoria = categoria

    def assegna_categoria(self):
        anno_corrente = date.today().year
        anno_di_nascita = datetime.strptime(self.data_di_nascita, '%d/%m/%Y').year
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
            categoria = 'under 30'