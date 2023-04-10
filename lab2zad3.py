liczby=[1,2,3,4,15,28,110,256,1]
p=[]

while liczby:
    p.append(str(liczby.pop()))

    p.sort(reverse=True)


while p:
    liczby.append(int(p.pop()))

print(liczby)