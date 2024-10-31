class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivut):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivut
    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi} Kirjoittaja: {self.kirjoittaja} Sivumäärä: {self.sivumaara}")

class Lehti(Julkaisu):
    def __init__(self, nimi, toimittaja):
        super().__init__(nimi)
        self.toimittaja = toimittaja
    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi} Toimittaja: {self.toimittaja}")

aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hyttinro6 = Kirja("Hytti nro 6", "Rosa Liksom", 200)
aku_ankka.tulosta_tiedot()
hyttinro6.tulosta_tiedot()
