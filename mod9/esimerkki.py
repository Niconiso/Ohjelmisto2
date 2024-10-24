
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
    def __init__(self, nimi, syntymävuosi, väri, koko):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.väri = väri
        self.koko = koko

k1 = Koira('lissu', 2015, 'harmaa', 'iso')
k2 = Koira('reko', 2016, 'ruskea', 'pieni')

print(k1.koko)