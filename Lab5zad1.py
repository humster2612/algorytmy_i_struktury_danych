def get(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>1:
        t=[0,1]
        i=2
        while(i<=n):
            t.append(t[i-1]+t[i-2])
            i+=1
        return t[i-1]
    else:
        print("podanie zle dane")
n=int(input("podaj n "))
print(get(n))
