def w_binarnu(liczba):
    if liczba ==0:
        return "0"
    
    else:
        reszta=liczba%2
        wynik=w_binarnu(liczba//2)
        return wynik+str(reszta)
    
liczba=int(input("Podaj liczbę dziesietna:"))
print(w_binarnu(liczba))
