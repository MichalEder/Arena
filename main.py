from bojovnik import Bojovnik
from kostka import Kostka
from arena import Arena
from mag import Mag
from barbar import Barbar


kostka = Kostka(10)
bojovnik_1 = Barbar("Datarios", 100, 20, 10, kostka, 1.5)
bojovnik_2 = Mag("Gandalf", 100, 20, 10, kostka, 100, 35)
arena = Arena(bojovnik_1, bojovnik_2, kostka)
arena.zapas()