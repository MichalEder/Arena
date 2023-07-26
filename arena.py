from barbar import Barbar
from mag import Mag

class Arena:
    def __init__(self, bojovnik_1, bojovnik_2, kostka):
        self._bojovnik_1 = bojovnik_1
        self._bojovnik_2 = bojovnik_2
        self._kostka = kostka

    def _vykresli(self):
        self._vycisti_obrazovku()
        print("-------------- Aréna -------------- \n")
        self._vypis_bojovnika(self._bojovnik_1)
        print()
        self._vypis_bojovnika(self._bojovnik_2)
        print()

    def _vypis_bojovnika(self, bojovnik):
        print(bojovnik)
        print(f"HP: {bojovnik.zivot_graficky()}")
        if isinstance(bojovnik, Mag):
            print(f"MP: {bojovnik.mana_graficky()}")
        elif isinstance(bojovnik, Barbar):
            print(f"Vtzek: {bojovnik.vztek_graficky()}")


    def _vycisti_obrazovku(self):
        import os
        if os.name == 'posix':  # For macOS and Linux
            os.system('clear')
        elif os.name == 'nt':  # For Windows
            os.system('cls')
        else:
            print("Sorry, your operating system is not supported.")

    def _vypis_zpravu(self, zprava):
        import time as _time
        print(zprava)
        _time.sleep(1.5)

    def zapas(self):
        import random as _random
        print("Lets get ready to rumbleeee!")
        print(f"Dnes se utkají {self._bojovnik_1} a {self._bojovnik_2}")
        print("Zápas může začít....")
        input()
        if _random.randint(0, 1):
            (self._bojovnik_1, self._bojovnik_2) = (self._bojovnik_2, self._bojovnik_1)
        while self._bojovnik_1.je_nazivu() and self._bojovnik_2.je_nazivu():
            self._bojovnik_1.utoc(self._bojovnik_2)
            self._vykresli()
            self._vypis_zpravu(self._bojovnik_1.vrat_posledni_zpravu())
            self._vypis_zpravu(self._bojovnik_2.vrat_posledni_zpravu())
            self._vycisti_obrazovku()
            if self._bojovnik_2.je_nazivu():
                self._bojovnik_2.utoc(self._bojovnik_1)
                self._vykresli()
                self._vypis_zpravu(self._bojovnik_2.vrat_posledni_zpravu())
                self._vypis_zpravu(self._bojovnik_1.vrat_posledni_zpravu())
            print("")



