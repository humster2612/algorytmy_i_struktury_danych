def NWD(a,b):
    while a!=b:
        if a>b:
            a=a-b
            NWD(a,b)

        else:
            b=b-a
            NWD(a,b)
    return a 
print(NWD(12,18))

