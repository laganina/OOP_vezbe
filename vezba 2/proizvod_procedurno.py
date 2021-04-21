def prikazi_proizvod(proizvod):
    print("\n".join([
        "",
        "{:>5}: {}".format("Sifra", proizvod["sifra"]),
        "{:>5}: {}".format("Naziv", proizvod["naziv"]),
        "{:>5}: {}".format("Cena", proizvod["cena"])
    ]))



def test():
    proizvod1 = {
        'sifra': '0001',
        'naziv': 'hleb',
        'cena': 50.0
    }
    proizvod2 = {
        'sifra':'0002',
        'naziv':'mleko 1l',
        'cena': 80.0
    }

    prikazi_proizvod(proizvod1)
    prikazi_proizvod(proizvod2)

    print()
    proizvod1["cena"] = float(input("Unesite novu cenu za proizvod {}:").format([proizvod1["naziv"]]))
    prikazi_proizvod(proizvod1)

if __name__ == '__main__':
    test()