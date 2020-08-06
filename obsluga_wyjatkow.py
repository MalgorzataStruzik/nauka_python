while True:
    try:
        print("Podaj liczbę: ")
        pierwsza = int(input())
        print("Podaj druga liczbe: ")
        druga = int(input())
        print(pierwsza + druga)
        break;
    except ValueError:
      print("podałes bledna wartosc")
      print("podaj jeszcze raz!")
      continue
