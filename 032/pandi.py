def noti(lista):
    for i in range(len(lista)):
        for j in range(0,i):
            if lista[i] == lista[j]:
                return False
    return True

arej=[]

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            for l in range(1,10):
                for m in range(1,10):
                    a = i*10 + j
                    b = k*100 + l*10 + m
                    c = a * b
                    if noti([i,j,k,l,m]) and len(str(c)) == 4:
                        cj = c//1000
                        ck = c//100  - cj*10
                        cl = c//10   - cj*100  - ck*10
                        cm = c//1    - cj*1000 - ck*100 - cl*10
                        if noti([i,j,k,l,m,cj,ck,cl,cm,0]):
                            if c not in arej:
                                arej.append(c)
                    a = i
                    b = j*1000 + k*100 + l*10 + m
                    c = a * b
                    if noti([i,j,k,l,m]) and len(str(c)) == 4:
                        cj = c//1000
                        ck = c//100  - cj*10
                        cl = c//10   - cj*100  - ck*10
                        cm = c//1    - cj*1000 - ck*100 - cl*10
                        if noti([i,j,k,l,m,cj,ck,cl,cm,0]):
                            if c not in arej:
                                arej.append(c)

suma=0

for i in arej:
    suma += i
    print(i)

print(suma)
