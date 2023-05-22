def zapisz_posortowane(liczba, lista_posortowana):
    liczba_binarna = bin(liczba)[2:]
    indeks = 0

    while indeks < len(lista_posortowana) and int(lista_posortowana[indeks], 2) < liczba:
        indeks += 1

    lista_posortowana.insert(indeks, liczba_binarna)

    return lista_posortowana

liczby = [5, 3, 9, 2, 7]
lista_posortowana = []

for liczba in liczby:
    lista_posortowana = zapisz_posortowane(liczba, lista_posortowana)

print(lista_posortowana)
