'''
koirat = [
    {'koira': 'Lissu', 'ikä': 3},
    {'koira': 'Reko', 'ikä': 7}
]

#print(koirat)
#eka_koira = koirat[0]
#print(eka_koira['koira'])

class Koira:
    pass
ullan_koira = Koira()
Elviiran_koira = Koira()

ullan_koira.nimi = 'Lissu'
ullan_koira.syntymävuosi = 2015
Elviiran_koira.nimi = 'Reko'
Elviiran_koira.syntymävuosi = 2016

print(f'Ullan koiran nimi on: {ullan_koira.nimi} ja syntymävuosi on {ullan_koira.syntymävuosi}')

class LuokanNimi:
    def __init__(self, parametri1, parametri2):
        self.attribuutti1 = parametri1
        self.attribuutti2 = parametri2

    def metodi(self):
        return
    def metodi2(self):
        return

class Koira:
    def __init__(self, nimi, syntymävuosi, väri, koko, haukahdus):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.väri = väri
        self.koko = koko
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        print(f'Koiran nimi on {self.nimi} ja haukkuu näin monta kertaa: {kerrat}')
        for i in range(kerrat):
            print(self.haukahdus)
        return

k1 = Koira('lissu', 2015, 'harmaa', 'iso', 'woof woof')
k2 = Koira('reko', 2016, 'ruskea', 'pieni', 'wiu wiu')

k1.hauku(5)
k2.hauku(6)'''

class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.nopeus = 0
        self.huippunopeus = huippunopeus
        self.kuljettaja = "Räikkönen"

    def tulosta_ominaisuudet(self):
        print(f"{self.rekkari}, huippunopeus, {self.huippunopeus}")
        print(f"Tämänhetkinen nopeus: {self.nopeus}")

    def kiihdytys(self, nopeuden_muutos):
        self.nopeus = self.nopeus + nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus