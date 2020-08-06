dziennik = {1:"Kowal",2:"Nowak",3:"Struzik"}

print(dziennik.get(1))
print(dziennik[1])
dziennik[4]="Mucha"
print(dziennik[4])

for key in dziennik.keys():
    print(key)

for value in dziennik.values():
    print(value)

del dziennik[1]

for value in dziennik.values():
    print(value)