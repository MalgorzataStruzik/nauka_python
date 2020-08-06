#programowanie obiektowe KLASA I OBIEKT

class Pies:

    gatunek = "pies domowy"

    def __init__(self,rasa,imie,wiek):
        self.rasa = rasa
        self.imie = imie
        self.wiek = wiek

reksio = Pies("kundel", "reksio",2)
print(reksio.wiek)
print(reksio.imie)