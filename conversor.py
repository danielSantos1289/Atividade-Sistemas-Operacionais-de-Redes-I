class Comprimento():

    def __init__(self, valor):
        self.valor = valor

    def quilometro(self):
        km = self.valor / 1000
        return km

    def centimetro(self):
        cm = self.valor * 100
        return cm

    def milimetro(self):
        mm = self.valor * 1000
        return mm


class Moedas:

    def __init__(self, real_):
        self.real = real_

    def dolar(self):
        dolar = self.real / 5.22
        return dolar

    def euro(self):
        euro = self.real / 6.29
        return euro

    def libra(self):
        libra = self.real / 6.95
        return libra

class Temperatura:

    def __init__(self, c_):
        self.c = c_

    def kelvin(self):
        k = (self.c + 273.15)
        return k

    def far(self) -> object:
        f = ((9 * self.c) / 5) + 32
        return f

    