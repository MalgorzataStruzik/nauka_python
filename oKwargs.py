def dziennik(klasa,**kwargs):
    print("klasa " + klasa)
    for nazwisko in kwargs.keys():
        print(nazwisko)
    print(kwargs.get("kowalski"))

dziennik("1c",kowalski="1",nowak="2")