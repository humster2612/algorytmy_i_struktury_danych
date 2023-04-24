def odwroc_tablice(tablica):
    i = 0
    j = len(tablica) - 1
    while i < j:
        tablica[i], tablica[j] = tablica[j], tablica[i]
        i += 1
        j -= 1
    return tablica
tablica = [1, 2, 3, 4, 5]
odwrocona_tablica = odwroc_tablice(tablica)
print(odwrocona_tablica)
