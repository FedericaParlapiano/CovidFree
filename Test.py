import unittest

from appuntamentotampone.model.AppuntamentoTampone import AppuntamentoTampone
from appuntamentovaccino.model.AppuntamentoVaccino import AppuntamentoVaccino
from calendariotamponi.controller.ControlloreCalendarioTamponi import ControlloreCalendarioTamponi
from calendariovaccini.controller.ControlloreCalendarioVaccini import ControlloreCalendarioVaccini
from cartellapaziente.model.CartellaPaziente import CartellaPaziente
from magazzino.controller.ControlloreMagazzino import ControlloreMagazzino
from statistiche.controller.ControlloreStatistiche import ControlloreStatistiche


class Test(unittest.TestCase):
    def setUp(self):
        self.controllore_calendario_vaccini = ControlloreCalendarioVaccini()
        self.controllore_calendario_tamponi = ControlloreCalendarioTamponi()
        self.controllore_magazzino = ControlloreMagazzino()
        self.controllore_statistiche = ControlloreStatistiche()

        self.elenco_appuntamenti_vaccini = self.controllore_calendario_vaccini.get_elenco_appuntamenti()
        self.elenco_appuntamenti_tamponi = self.controllore_calendario_tamponi.get_elenco_appuntamenti()
        self.elenco_materiali = self.controllore_magazzino.get_magazzino()
        self.elenco_dati_statistiche = self.controllore_statistiche.get_dati_tamponi()

        self.cartella = CartellaPaziente(nome="Enrico", cognome="Corradini", data_di_nascita="15/03/1960", cf="CRRDNERC", indirizzo="Via Brecce Bianche", telefono="071 220 4128", categoria=" ", preferenza="Astrazeneca",
                                         anamnesi={'Pfizer': 'Si', 'Moderna': 'Si', 'Astrazeneca': 'No', 'Reazione grave': 'No', 'Malattie': 'No', 'Sistema immunitario': 'No', 'Gravidanza': 'No', 'Contatto': 'No', 'Sintomi': 'No', 'Positivo COVID-19': 'mai'})
        self.appuntamento_vaccino = AppuntamentoVaccino(id="Prima Dose", cartella_paziente=self.cartella, data_appuntamento="04-07-2021", fascia_oraria="9:00-10:00", is_a_domicilio=False)
        self.appuntamento_tampone = AppuntamentoTampone(nome="Domenico", cognome="Ursino", cf="URSNDMNC0", telefono="071 567896", indirizzo="via Brecce Bianche", data_nascita="08/12/1995", data_appuntamento="2021-07-04", fascia_oraria="9:00-10:00", is_drive_through=True, tipo_tampone="Sierologico")
        self.risultati_tampone = ['Positivo', 'Sì']

    # Test che controlla se un appuntamento per un vaccino è stato inserito correttamente.
    def test_inserisci_appuntamento_vaccino(self):
        self.assertIsNotNone(self.appuntamento_vaccino.vaccino)
        self.controllore_calendario_vaccini.aggiungi_appuntamento(self.appuntamento_vaccino)
        self.assertTrue(self.appuntamento_vaccino in self.elenco_appuntamenti_vaccini)

    # Test che verifica la corretta ricerca dell'appuntamento per il vaccino.
    def test_ricerca_appuntamento_vaccino(self):
        self.assertIsNotNone(self.elenco_appuntamenti_vaccini)
        trovato = self.controllore_calendario_vaccini.get_appuntamento_by_cf(self.appuntamento_vaccino.cartella_paziente.nome,
                                                                             self.appuntamento_vaccino.cartella_paziente.cognome,
                                                                             self.appuntamento_vaccino.cartella_paziente.cf,
                                                                             self.appuntamento_vaccino.id)
        self.assertTrue(trovato, self.appuntamento_vaccino)

    # Test che verifica la corretta eliminazione dell'appuntamento per il vaccino.
    def test_elimina_appuntamento_vaccino(self):
        self.assertIsNotNone(self.elenco_appuntamenti_vaccini)
        self.controllore_calendario_vaccini.elimina_appuntamento(self.appuntamento_vaccino)
        self.assertTrue(self.appuntamento_vaccino not in self.elenco_appuntamenti_vaccini)

    # Test che controlla se un appuntamento per un tampone è stato inserito correttamente.
    def test_inserisci_appuntamento_tampone(self):
        self.assertIsNotNone(self.appuntamento_tampone.tipo_tampone)
        self.controllore_calendario_tamponi.aggiungi_appuntamento(self.appuntamento_tampone)
        self.assertTrue(self.appuntamento_tampone in self.elenco_appuntamenti_tamponi)

    # Test che verifica la corretta ricerca dell'appuntamento per un tampone.
    def test_ricerca_appuntamento_tampone(self):
        self.assertIsNotNone(self.elenco_appuntamenti_tamponi)
        trovato = self.controllore_calendario_tamponi.get_appuntamento_by_cf(self.appuntamento_tampone.nome,
                                                                             self.appuntamento_tampone.cognome,
                                                                             self.appuntamento_tampone.data_nascita,
                                                                             self.appuntamento_tampone.cf,
                                                                             self.appuntamento_tampone.tipo_tampone)
        self.assertTrue(trovato, self.appuntamento_tampone)

    # Test che verifica la corretta eliminazione dell'appuntamento per il tampone.
    def test_elimina_appuntamento_tampone(self):
        self.assertIsNotNone(self.elenco_appuntamenti_tamponi)
        self.controllore_calendario_tamponi.elimina_appuntamento(self.appuntamento_tampone)
        self.assertTrue(self.appuntamento_tampone not in self.elenco_appuntamenti_tamponi)

    # Test che verifica il corretto aggiornamento del magazzino.
    def test_aggiorna_magazzino(self):
        quantita_iniziale = self.controllore_magazzino.get_presidio_by_index(2).quantita
        quantita_da_aggiungere = 5
        self.controllore_magazzino.aggiorna_quantita_by_tipologia("Pfizer", quantita_da_aggiungere)
        self.assertEqual(quantita_iniziale + quantita_da_aggiungere, self.controllore_magazzino.get_presidio_by_index(2).quantita)

    # Test che verifica il corretto inserimento dei dati ai fini delle statistiche sui tamponi.
    def test_inserisci_dati_tampone_statistiche(self):
        self.assertIsNotNone(self.elenco_dati_statistiche)
        self.controllore_statistiche.salva_dati_tamponi(self.risultati_tampone)
        self.assertTrue(self.risultati_tampone in self.elenco_dati_statistiche)




if __name__ == '__main__':
    unittest.main()
