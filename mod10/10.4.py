import random

class Auto:
    def __init__(self, nimi, Hnopeus):
        self.nimi = nimi
        self.huippunopeus = Hnopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        self.nopeus = max(0, min(self.huippunopeus, self.nopeus + muutos))

    def kulje(self):
        self.matka += self.nopeus

class Kilpailu:
    def __init__(self, nimi, kilometrit, autot):
        self.nimi = nimi
        self.pituus_km = kilometrit
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje()

    def tulosta_tilanne(self):
        print(f"{'Auto':<15}{'Nopeus (km/h)':<15}{'Matka (km)':<15}")
        for auto in self.autot:
            print(f"{auto.nimi:<15}{auto.nopeus:<15}{auto.matka:<15}")


    def kilpailu_ohi(self):
        return any(auto.matka >= self.pituus_km for auto in self.autot)

autot = [Auto(f"Auto {i+1}", random.randint(100, 200)) for i in range(10)]
kilpailu = Kilpailu("", 8000, autot)

tunti = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunti += 1
    if tunti % 10 == 0:
        print(f"\nTunti {tunti}")
        kilpailu.tulosta_tilanne()

print("\nKilpailu päättyi!")
kilpailu.tulosta_tilanne()
