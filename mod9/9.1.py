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

kaara = Auto("ABC-123", 142)
kaara.tiedot()
