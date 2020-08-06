#generator liczb losowych

import random

def generuj_licze(min,max):
    return random.randint(min,max)

for i in range(0,20):
    print(generuj_licze(0,100))
