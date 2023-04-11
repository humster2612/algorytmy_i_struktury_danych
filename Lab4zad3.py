def g(wektor,p,q):
    if p==q:
        return wektor[p]
    elif (p+1)==q:
        return max(wektor[p],wektor[q])
    else:
        mid = (p + q) // 2
        max1 = g(wektor, p, mid)
        max2 = g(wektor, mid+1, q)
        return max(max1, max2)

wektor = []
liczby = int(input("Podaj ilość liczb: "))
for i in range(liczby):
    a = int(input("Podaj: "))
    wektor.append(a)
g(wektor, 0, liczby - 1)
print(g(wektor, 0, liczby - 1))
