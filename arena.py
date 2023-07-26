class Arena:
    def __init__(self, bojovnik_1, bojovnik_2, kostka):
        self._bojovnik_1 = bojovnik_1
        self._bojovnik_2 = bojovnik_2
        self._kostka = kostka

    def _vykresli(self):
        self._vycisti_obrazovku()
        print("-------------- Aréna -------------- \n")
        print("Zdraví bojovníků: \n")
        print(f"Jmeno: {self._bojovnik_1} HP: {self._bojovnik_1.zivot_graficky()} Rage: {self._bojovnik_1.graficky_vztek()}")
        print(f"Jmeno: {self._bojovnik_2} HP: {self._bojovnik_2.zivot_graficky()} MP: {self._bojovnik_2.mana_graficky()}")
    def _vycisti_obrazovku(self):
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith("win"):
            _subprocess.call(["cmd.exe", "/C", "cls"])
        else:
            _subprocess.call(["clear"])
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
            if self._bojovnik_2.je_nazivu():
                self._bojovnik_2.utoc(self._bojovnik_1)
                self._vykresli()
                self._vypis_zpravu(self._bojovnik_2.vrat_posledni_zpravu())
                self._vypis_zpravu(self._bojovnik_1.vrat_posledni_zpravu())
            print("")



