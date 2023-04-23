def zad5(n, A, B, C):
    if n == 1:
        print(f"Przenies krążek z {A} na {C}")
    else:
        zad5(n-1, A, C, B)
        print(f"Przenies krążek z {A} na {C}")
        zad5(n-1, B, A, C)
zad5(int(input('podaj ilość krążek:')), 'A', 'B', 'C')
