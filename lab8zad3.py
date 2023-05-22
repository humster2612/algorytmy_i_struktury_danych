def sorted_lists(lista_p, lista_d):
    listy = []
    i = 0
    j = 0

    while i < len(lista_p) and j < len(lista_d):
        if lista_p[i] <= lista_d[j]:
            listy.append(lista_p[i])
            i += 1
        else:
            listy.append(lista_d[j])
            j += 1
    listy.extend(lista_p[i:])
    listy.extend(lista_d[j:])

    return listy
lista_p = [10,2,3,5,6,8,32,156]
lista_d = [1,134,932,7,9,11,52,23]

listy = sorted_lists(sorted(lista_p), sorted(lista_d))
print(listy)
