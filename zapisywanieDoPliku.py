file = open("nowy.txt","w")

# ("nowy.txt","w") -- piszemy w pliku, nadpisujemy
# ("nowy.txt","a") --dodajemy tekst do istniejącego tekstu
file.write("trutu tutut")
file.close()