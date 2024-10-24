class Auto:
    def __init__(self, rekkari, hnopeus):
        self.rekisteritunnus = rekkari
        self.huippunopeus = hnopeus
        self.Tnopeus = 0
        self.matka = 0

    def tiedot(self):
        print(f"Rekkari: {self.rekisteritunnus}")
        print(f"Huippunopeus: {self.huippunopeus} km/h")
        print(f"Tämänhetkinen nopeus: {self.Tnopeus} km/h")
        print(f"Matka: {self.matka} km")

    def kiihdytä(self, muutos):
        self.Tnopeus += muutos
        if self.Tnopeus > self.huippunopeus:
            self.Tnopeus = self.huippunopeus
        elif self.Tnopeus < 0:
            self.Tnopeus = 0
        print(f"Nopeus: {self.Tnopeus} km/h")

    def kulje(self, aika):
        Kmatka = self.Tnopeus * aika
        self.matka += Kmatka
        print(f"Matka on {Kmatka} km, kuljettu matka yhteensä {self.matka} km")
kaara = Auto("ABC-123", 142)
kaara.matka = 2000
kaara.kiihdytä(60)
kaara.kulje(1.5)
kaara.tiedot()
