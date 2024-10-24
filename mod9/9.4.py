import random

class Auto:
    def __init__(self, rekkari, hnopeus):
        self.rekkari = rekkari
        self.huippunopeus = hnopeus
        self.Tnopeus = 0
        self.matka = 0


    def kiihdytys(self, muutos):
        self.Tnopeus += muutos
        if self.Tnopeus > self.huippunopeus:
            self.Tnopeus = self.huippunopeus

        elif self.Tnopeus < 0:
            self.Tnopeus = 0

    def kulje(self, aika):
        Kmatka = self.Tnopeus * aika
        self.matka += Kmatka

kaara = []
for i in range(1, 11):
    rekkari = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    kaara.append(Auto(rekkari, huippunopeus))

kilpailu = True
while kilpailu:
    for auto in kaara:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdytys(nopeuden_muutos)
        auto.kulje(1)
        if auto.matka >= 10000:
            kilpailu = False
            break

print(f"{'Rekkari':<10} {'Huippunopeus':<15} {'Nopeus':<10} {'Matka':<10}")
for auto in kaara:
    print(f"{auto.rekkari:<10} {auto.huippunopeus:<15} {auto.Tnopeus:<10} {auto.matka:<10}")
