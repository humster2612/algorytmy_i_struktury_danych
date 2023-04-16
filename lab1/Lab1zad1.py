import math
a = int(input("Podaj współczynnik a: "))
b = int(input("Podaj współczynnik b: "))
c = int(input("Podaj współczynnik c: "))
if a != 0:
    D = b*b - 4 * a * c
    if D > 0:
        x1 = (-b + math.sqrt(D))/(2 * a)
        x2 = (-b - math.sqrt(D))/(2 * a)
        print(f"Rozwiązania równania: x1 = {x1}, x2 = {x2}")
    elif D == 0:
        x = -b/(2 * a)
        print(f"Rozwiązanie równania: x = {x}")
    else:
        print("Błąd rozwiązań rzeczywistych")
else:
    print("Nie jest równaniem kwadratowym")
