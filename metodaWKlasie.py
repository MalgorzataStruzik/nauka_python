#programowanie obiektowe KLASA I OBIEKT

class Pies:

    gatunek = "pies domowy"

    def __init__(self,rasa,imie,wiek):
        self.rasa = rasa
        self.imie = imie
        self.wiek = wiek

    def szczekaj(self):
        return "hau hau!"

    def reprezentuj_psa(self):
        print("rasa to: " + self.rasa)
        print("imie to : " + self.imie)
        print("wiek psa to: " + str(self.wiek))



reksio = Pies("kundel", "reksio",2)
print(reksio.wiek)
print(reksio.imie)

print(reksio.szczekaj())
print(reksio.reprezentuj_psa())