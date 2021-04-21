class Proizvod:

    @property
    def cena(self):
        return self.__cena

    @cena.setter
    def cena(self, cena):
        self.__cena = cena



    def __init__(self, sifra, naziv, cena):
        self.__sifra = sifra
        self.__naziv = naziv
        self.__cena = cena

    def __str__(self):
        return "\n".join([
            "",
            "{:>5}: {}".format("Sifra", self.__sifra),
            "{:>5}: {}".format("Naziv", self.__naziv),
            "{:>5}: {}".format("Cena", self.__cena)
        ])

def test():

    proizvod1 = Proizvod("0001", "hleb", 50.0)
    print(proizvod1)
    proizvod1.cena = 100.0
    print(proizvod1.cena)

if __name__ == '__main__':

    test()