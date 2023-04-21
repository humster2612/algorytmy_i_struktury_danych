n = int(input("Podaj liczbę n: "))
ilosc_ujemnych = 0
liczby = []
i = 0
while i < n:
    liczba= int(input(f"Podaj {i+1}. liczbę: "))
    liczby.append(liczba)
    if liczba< 0:
        ilosc_ujemnych += 1
    i+=1
print(f"Ilość liczb ujemnych w ciągu wynosi: {ilosc_ujemnych}")
