class Auto:
    def __init__(self, rekkari, Hnopeus):
        self.rekkari = rekkari
        self.huippunopeus = Hnopeus
        self.nopeus = 0
        self.matkamittari = 0

    def aseta_nopeus(self, nopeus):
        if nopeus <= self.huippunopeus:
            self.nopeus = nopeus
        else:
            self.nopeus = self.huippunopeus
    def aja(self, tunnit):
        self.matkamittari += self.nopeus * tunnit

class Sahkoauto(Auto):
    def __init__(self, rekkari, Hnopeus, akku):
        super().__init__(rekkari, Hnopeus)
        self.akku = akku

class Polttomoottoriauto(Auto):
    def __init__(self, rekkari, Hnopeus, bensatankki):
        super().__init__(rekkari, Hnopeus)
        self.bensatankki = bensatankki

SähAuto = Sahkoauto("ABC-15", 180, 52.5)
PerusAuto = Polttomoottoriauto("ACD-123", 165, 32.3)
SähAuto.aseta_nopeus(150)
PerusAuto.aseta_nopeus(120)
SähAuto.aja(3)
PerusAuto.aja(3)
print(f"Sähköauto {SähAuto.rekkari} matkamittarilukema: {SähAuto.matkamittari} km")
print(f"Polttomoottoriauto {PerusAuto.rekkari} matkamittarilukema: {PerusAuto.matkamittari} km")