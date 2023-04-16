def razem(tabela, n):
    
    if n==0:
        return 0
    
    elif n==1:
        return tabela[0]
    

    else:
        mid=n//2
        f=n-mid
        left_sum = razem(tabela, mid)

        right_sum = razem(tabela[mid:n],f)
        return right_sum + left_sum

tabela = []

a = int(input("Podaj ilość w tabele: "))


for i in range(a):
    c= int(input("Podaj liczby N: "))
    tabela.append(c)

print(razem(tabela, a))