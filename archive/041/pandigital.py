from itertools import permutations as perm
from math import factorial as fac
from math import ceil, sqrt
import collections

nn = 10**5

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

def giveme(howmany,which):
    i = howmany+1
    j = which-1
    stringu = ""
    for k in range(howmany):
        stringu += str(list(perm(range(1,i)))[j][k])
    return stringu

# for n in range(8,10):
#     for i in range(fac(n)):
#         z = int(giveme(n,i))
#         if easyif(z):
#             print(z)


def checkpandigi(n):
    en = str(n)
    length = len(en)
    array = sorted(list(en))
    for i in range(length):
        if not array[i] == str(i+1):
            return False
    return True

for i in range(10**7):
    if checkpandigi(i):
        if genif(i):
            print(i)
