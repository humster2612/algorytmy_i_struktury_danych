p = int(input("Podaj liczbę p: "))
q = [int(input("Podaj liczbę: ")) for i in range(p)]
i = 0
min = q[1]
while i < p:
    if q[i] < min:
        min = i
print(min)
 