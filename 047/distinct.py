from math import ceil, sqrt

nn = 700

def easyif(n):
    if n == 1:
        return False
    if n in (2,3,5):
        return True
    if n%2 == 0:
        return False
    if n%3 == 0:
        return False
    if n%5 == 0:
        return False
    for i in range(7,int(ceil(sqrt(n)))):
        if n%i == 0:
            return False
    return True

biglist=[]
for i in range(2,nn):
    if easyif(i):
        biglist.append(i)

def hardif(n):
    for i in biglist:
        if n%i == 0:
            return False
    return True

def genif(n):
    global nn
    if n<nn:
        return easyif(n)
    else:
        return hardif(n)

def find2prime(n):
    half = 0
    lista = []
    for i in biglist:
        if i>n:
            return False
        if n%i == 0:
            half +=1
            n = n/i
            lista.append(i)
            if half == 4:
                return True

go = 0
for i in range(1,700**2):
    if find2prime(i):
        go += 1
        if go == 4:
            print(i-3)
            break
    else:
        go = 0
