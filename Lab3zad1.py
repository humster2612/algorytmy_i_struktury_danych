def sil(a):
    if (a == 0):
        return 1 
   else:
        return sil(a - 1) * a
print(sil(int(input("Podaj liczbę:"))))
