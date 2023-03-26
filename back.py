from enum import Enum
class Miesiace(Enum):
    STYCZEN = 1
    LUTY = 2
    MARZEC = 3
    KWIECIEN = 4
    MAJ = 5
    CZERWIEC = 6
    LIPIEC = 7
    SIERPIEN = 8
    WRZESIEN = 9
    PAZDZIERNIK = 10
    LISTOPAD = 11
    GRUDZIEN = 12

class Czlowiek():
    def __init__(self, imie:str,naziwsko:str,wiek:int,rokUrodzenia:Miesiace,pesel = None) -> None:
        self.imie = imie
        self.naziwsko = naziwsko
        self.wiek = wiek
        self.pesel = pesel
        self.rokUrodzenia = rokUrodzenia
    def __str__(self) -> str:
        peselStr = str(self.pesel) if self.pesel is not None else "brak"
        pesel = f"pesel: {self.pesel}" if len(peselStr) == 11 else "Pesel: brak"
        return f"Imie: {self.imie}, naziwsko: {self.naziwsko}, wiek: {self.wiek}, rok urodzenia: {self.rokUrodzenia.name}, {pesel}"