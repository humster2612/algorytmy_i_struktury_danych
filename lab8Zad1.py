def wyszukaj_binarnie(lista, szukana):
    posortowana_lista = sorted(lista)
    lewy = 0
    prawy = len(posortowana_lista) - 1

    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        if posortowana_lista[srodek] == szukana:
            return srodek
        elif posortowana_lista[srodek] < szukana:
            lewy = srodek + 1
        else:
            prawy = srodek - 1

    return -1


lista = [20, 4, 10, 16, 2, 14, 8, 6, 18, 12]
szukana_wartosc = int(input('Podaj szukaną wartość:'))

indeks = wyszukaj_binarnie(lista, szukana_wartosc)
if indeks != -1:
    print("Znaleziono wartość na indeksie:", indeks)
else:
    print("Wartość nie została znale
