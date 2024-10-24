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
        print(f"Nopeus: {self.Tnopeus} km/h\n")
kaara = Auto("ABC-123", 142)
kaara.kiihdytä(30)
kaara.kiihdytä(70)
kaara.kiihdytä(50)
kaara.kiihdytä(-200)
kaara.tiedot()
