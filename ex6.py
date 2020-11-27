# Magazyn książek
class Paczka:
    def __init__(self, klient):
        self.__klient = klient
        self.__zawartosc = []

    def dodaj(self, ksiazka):
        self.__zawartosc.append(ksiazka)

    def wlasciciel(self):
        return self.__klient

    def ksiazki(self):
        return self.__zawartosc

    def zawartosc(self):
        print("Paczka:")
        print("%s %s" % self.__klient.dajInfo())
        print("-" * 50)
        for ksiazka in paczka.ksiazki():
            print("Tytuł: %s Cena: %f" % ksiazka.dajInfo())


class Klient:
    def __init__(self, nazwa, adres):
        self.__nazwa = nazwa
        self.__adres = adres

    def dajInfo(self):
        return self.__nazwa, self.__adres


class Sprzedawca:
    def dodajKsiazke(self, ksiazka, paczka):
        paczka.dodaj(ksiazka)

    def oddajKsiazke(self, ksiazka, paczka):
        pass

    def finalizuj(self, paczka):
        wlasciciel = paczka.wlasciciel()
        print("=" * 40)
        paczka.zawartosc()
        suma = 0.0
        for ksiazka in paczka.ksiazki():
            suma += ksiazka.dajInfo()[1]
        print("-" * 40)
        print("Suma: %f" % suma)
        print("-" * 40)


class Ksiazka:
    def __init__(self, nazwa, cena):
        self.__nazwa = nazwa
        self.__cena = cena

    def dajInfo(self):
        return self.__nazwa, self.__cena


if __name__ == '__main__':
    klient = Klient("Adam", "01-001 Koluszki, ul Błotna 12")
    sprzedawca = Sprzedawca()
    paczka = Paczka(klient)

    ksiazka1 = Ksiazka("Przygody w kuchni", 120.5)
    ksiazka2 = Ksiazka("Młot na czarownice", 350.1)

    sprzedawca.dodajKsiazke(ksiazka1, paczka)
    sprzedawca.dodajKsiazke(ksiazka2, paczka)

    sprzedawca.finalizuj(paczka)
