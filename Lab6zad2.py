import random
m=int(input('podaj długość'))
tablica = []
i=0
while i<(m//2):
    tablica.append(random.randint(0,99))
    i+=1
i=0
while i<(m//2):
    tablica.append(tablica[i])
    i+=1
print(tablica)
