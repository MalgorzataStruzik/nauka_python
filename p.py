poprzedni = 0

for i in range(1,11):  
    i = poprzedni + i
    print(f'{i}')
    poprzedni = i
