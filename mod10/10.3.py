class Hissi:
    def __init__(self, Akerros, Ykerros):
        self.alin_kerros = Akerros
        self.ylin_kerros = Ykerros
        self.nykyinen_kerros = Akerros

    def siirtyminen(self, kohde):
        while self.nykyinen_kerros < kohde:
            self.KerrosY()
        while self.nykyinen_kerros > kohde:
            self.KerrosA()

    def KerrosY(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def KerrosA(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumäärä):
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lukumäärä)]

    def aja_hissiä(self, hissin_numero, kohde_kerros):
        self.hissit[hissin_numero].siirtyminen(kohde_kerros)

    def palohälytys(self):
        print("Palohälytys")
        for hissi in self.hissit:
            hissi.siirtyminen(self.hissit[0].alin_kerros)

talo = Talo(1, 10, 3)
talo.aja_hissiä(0, 5)
talo.aja_hissiä(1, 8)
talo.aja_hissiä(2, 3)
talo.palohälytys()
