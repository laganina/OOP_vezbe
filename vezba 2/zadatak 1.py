class Osoba:

    def __init__(self, jmbg, ime, prezime, grodjenja):
        self.__jmbg = jmbg
        self.__ime = ime
        self.__prezime = prezime
        self.__grodjenja = grodjenja

    def __str__(self):
        return "\n".join([
            "",
            "{:>13: {}".format("JMBG", self.__sifra),
            "{:>10: {}".format("Ime", self.__ime),
            "{:>10: {}".format("Prezime", self.__prezime),
            "{:>13: {}".format("God rodjenja", self.__grodjenja)
        ])

    @property
    def jmbg(self):
        return self.__jmbg
    @jmbg.setter
    def jmbg(self,jmbg):
        self.__jmbg = jmbg

    @property
    def ime(self):
        return self.__ime
    @ime.setter
    def ime(self,ime):
        self.__ime = ime

    @property
    def prezime(self):
        return self.__prezime
    @prezime.setter
    def prezime(self, prezime):
        self.__prezime = prezime

    @property
    def grodjenja(self):
        return self.__grodjenja
    @grodjenja.setter
    def grodjenja(self,grodjenja):
        self.__grodjenja = grodjenja

def test(self):
        osoba1 = Osoba("1111111111111", "Aaa", "Aaa",2001)
        osoba2 = Osoba("2222222222222", "Bbb", "Bbb", 2002)
        osoba3 = Osoba("3333333333333", "Ccc", "Ccc", 2003)

        print()
        osoba1.jmbg = input("Unesite novi JMBG za osobu 1: ")
        osoba1.ime = input("Unesite novo ime za osobu 1: ")
        osoba1.prezime = input("Unesite ovo prezime za osobu 1: ")
        osoba1.grodjenja = int(input("Unesite novu godinu rodjenja za osobu 1: "))
        print()

        print("Novi JMBG osobe1 je: ", osoba1.jmbg)
        print("Novo ime osobe 1 je: ", osoba1.ime)
        print("Novo prezime osobe 1 je: ", osoba1.prezime)
        print("Nova godina rodjenja osobe 1 je: ", osoba1.grodjenja)

        osobe = [
            osoba1,
            osoba2,
            osoba3
        ]

        for osoba in osobe:
            print(osoba)


