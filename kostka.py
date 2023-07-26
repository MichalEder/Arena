class Kostka:
    """
    Třída reprezentuje hrací kostku

    """
    def __init__(self, pocet_sten=6):
        self.__pocet_sten = pocet_sten


    def vrat_pocet_sten(self):
        """
        Vrátí počet stěn
        """
        return self.__pocet_sten
        
        
    def hod(self):
        """
        Vykoná hod kostkou a vrátí náhodné hozené číslo v rozmezí 1-počet stěn kostky
        """
        import random as _random
        return _random.randint(1, self.__pocet_sten)
        
    def __str__(self):
        """
        Vrací textovou reprezentaci kostky
        """
        return str(f"Kostka s {self.__pocet_sten} stěnami")

