def NWD (a,b):
    while b!=0:
        c=b
        b=a%b
        a=c
        NWD(a,b)

    return a
print(NWD(3,6))
