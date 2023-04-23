a=int(input("Podaj a : "))
b=int(input("Podaj b : "))
if b==0:
    print("NWD jest: ",a)

elif a < 0 or b < 0:
    print("Nie może tak być! ")

else:

    while b>0:
        reszta = a%b
        a=b
        b=reszta
    print("NWD jest: ",a )
