from math import ceil, sqrt
from itertools import permutations as perm
from sys import exit as ex

nn = 100

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

for i in range(1000,3333):
    if genif(i):
        for j in range(10,5000):
            if genif(i+j) and genif(i+2*j):
                lista = list(perm(list(str(i))))
                if tuple(str(i+j)) in lista and tuple(str(i+2*j)) in lista:
                    print(i,i+j,i+2*j)
