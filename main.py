from bojovnik import Bojovnik
from kostka import Kostka

kostka = Kostka(10)

bojovnik_1 = Bojovnik("Datarios", 100, 20, 10, kostka)
bojovnik_2 = Bojovnik("Warlord", 100, 20, 10, kostka)

print(f"Bojovnik: {bojovnik_1}")
print(f"Je naživu: {bojovnik_1.je_nazivu()}")
print(f"Počet životů: {bojovnik_1.zivot_graficky()}")
bojovnik_1.utoc(bojovnik_2)
print(bojovnik_1.vrat_posledni_zpravu())
print(bojovnik_2.vrat_posledni_zpravu())