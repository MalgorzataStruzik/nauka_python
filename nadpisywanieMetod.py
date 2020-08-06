# metoda z klasy rodzica zostala nadpisana z metody dziecka
class Osoba:

    def __init__(self,imie,nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "Nazywam się " + self.imie + " " + self.nazwisko

class Student(Osoba):
    def __init__(self, imie, nazwisko, numer_indeksu):
        Osoba.__init__(self, imie, nazwisko)
        self.indeks = numer_indeksu

    def podaj_numer_indeksu(self):
        return self.indeks

    def przedstaw_sie(self):
        return "jestem studentem i mam na imię " + self.imie


student = Student("Tomasz","Kot",123345)
print(student.przedstaw_sie())
print(student.podaj_numer_indeksu())
