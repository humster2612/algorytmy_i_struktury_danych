q = int(input("Podaj  liczbę q: "))
p = [int(input("Podaj liczbę: ")) for i in range(q)]
i = 0
ile_u = 0
for i in p:
    if i < 0:
        ile_u += 1
        i += 1
    else:
        i += 1
print(f"Ilość ujemnych liczb  będę: {ile_u}")
