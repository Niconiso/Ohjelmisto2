class Hissi:
    def __init__(self, Akerros, Ykerros):
        self.alin_kerros = Akerros
        self.ylin_kerros = Ykerros
        self.nykyinen_kerros = Akerros

    def siirtyminen(self, kerros):
        while self.nykyinen_kerros < kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kerros:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

hissi = Hissi(1, 10)
hissi.siirtyminen(5)
hissi.siirtyminen(1)

