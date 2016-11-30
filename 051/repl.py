from math import ceil, sqrt
from sys import exit as ex

nn = 2*10**5

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
    for i in range(7,int(ceil(sqrt(n)+1))):
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

def checker(n,cos):
    lista = list(str(n))
    suma = 0
    for j in range(10):
        for i in cos:
            lista[i] = str(j)
        value = int(''.join(lista))
        if genif(value):
            suma += 1
    return suma

nnn = 6
for k in range(0,nnn):
    for l in range(k+1,nnn):
         for m in range(l+1,nnn):
                    max = 0
                    for j in range(10**(nnn-1),2*10**(nnn-1)):
                        val = checker(j,(k,l,m))
                        if val>max:
                            max = val
                            print(k,l,m,j,val)
                            if val==8:
                                print("OH baby")
                                ex()
