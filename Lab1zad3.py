q= int(input("Podaj liczbę q: "))
p = int(input("Podaj liczbę wyszukiwaną: "))
A = [int(input("Podaj liczbę: ")) for i in range(q)]
l = 0
while l < q:
    if A[l]==p:
        print("Liczba wyszukiwana występuje w liście")
        break
    else:
        l += 1
        continue
else:
    print("Liczba wyszukiwana nie występuje w liście")

