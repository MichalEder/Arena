from bojovnik import Bojovnik


class Barbar(Bojovnik):
    def __init__(self, jmeno, zivot, utok, obrana, kostka, sila, vztek=0):
        super().__init__(jmeno, zivot, utok, obrana, kostka)
        self._vztek = vztek
        self._max_vztek = 100
        self._silny_utok = int(utok * sila)

    def utoc(self, souper):
        if self._vztek < 60:
            if self._vztek > self._max_vztek:
                self._vztek = self._max_vztek
            uder = self._utok + self._kostka.hod()
            zprava = f"{self._jmeno} útočí za {uder}hp"
            self._nastav_zpravu(zprava)
        else:
            uder = self._silny_utok + self._kostka.hod()
            zprava = f"{self._jmeno} používá drtivý úder za {uder}hp"
            self._nastav_zpravu(zprava)
            self._vztek -= 50
        souper.bran_se(uder)

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
                self._vztek += zraneni
        else:
            zprava = zprava + f", který odrazil"
        self._nastav_zpravu(zprava)

    def graficky_vztek(self):
        return self.graficky_ukazatel(self._vztek, self._max_vztek)