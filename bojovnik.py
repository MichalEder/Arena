class Bojovnik:
    """ Třída reprezentující bojovníka v aréně. """
    def __init__(self, jmeno, zivot, utok, obrana, kostka):
        self._jmeno = jmeno
        self._zivot = zivot
        self._max_zivot = zivot
        self._utok = utok
        self._obrana = obrana
        self._kostka = kostka
        self._zprava = ""

    def _nastav_zpravu(self, zprava):
        self._zprava = zprava


    def vrat_posledni_zpravu(self):
        return self._zprava

    def __str__(self):
        return str(self._jmeno)

    def je_nazivu(self):
        return self._zivot > 0

    def zivot_graficky(self):
        return self.graficky_ukazatel(self._zivot, self._max_zivot)


    def bran_se(self, uder):
        zraneni = uder - (self._obrana + self._kostka.hod())
        zprava = f"{self._jmeno} se brání útoku za {uder}hp"
        if zraneni > 0:
            self._zivot -= zraneni
            zprava = zprava + f" a utrpěl zranění {zraneni}"
            if self._zivot < 0:
                self._zivot = 0
                zprava = zprava + f", které pro něj bylo fatální....umírá."
            else:
                zprava = zprava + f", které ještě přežil."
        else:
            zprava = zprava + f", který odrazil"
        self._nastav_zpravu(zprava)

    def utoc(self, souper):
        uder = self._utok + self._kostka.hod()
        zprava = f"{self._jmeno} utocí za {uder}hp"
        self._nastav_zpravu(zprava)
        souper.bran_se(uder)

    def graficky_ukazatel(self, aktualni, maximalni):
        celkem = 20
        pocet = int((aktualni/ maximalni) * celkem)
        if (pocet == 0 and self.je_nazivu()):
            pocet = 1
        return "[{0}{1}]".format("#" * pocet, " " * (celkem - pocet))




