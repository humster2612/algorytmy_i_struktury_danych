suma_parzysta = 0
suma_nie_parzysta = 0
i = 1
while i <21:
    liczba = int(input(f'podaj {i} leczbę'))
    if liczba%2 == 1:
        suma_nie_parzysta+=liczba
    else:
        suma_parzysta+=liczba
    i+=1
print(f'suma parzysta:{suma_parzysta}')
print(f'suma nie parzysta:{suma_nie_parzysta}')
