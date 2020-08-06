# lista

imiona = ["Ola","Kasia","Stasia"]

for i in imiona:
    print(i)

imiona.append("Staś") #dodanie elementu do listy
imiona.insert(0,"Lola")
print(imiona)
imiona.remove("Ola")
print(imiona)

# sortowanie listy

imiona.sort()
print(imiona)

posortowane = sorted(imiona, reverse=True)
print(posortowane)

#można też w print dodawac do siebie listy