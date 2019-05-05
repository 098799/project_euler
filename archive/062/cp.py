from itertools import permutations
from sys import exit
from collections import Counter
from time import time

def isCube(n):
    en = n**(1/3)
    if en == en//1:
        return True
    return False

def isPerm(n,m):
    en = Counter(list(str(n)))
    em = Counter(list(str(m)))
    if en == em: return True
    return False

cubeList = []
for i in range(10**3):
    cubeList.append(i**3)


n = 7
t0 = time()
while True:

    n +=1

    i = n//3
    maxval = 0

    while i**3<10**(n+1):
        i += 1
        val = i**3
        if val < 10**n:
            continue
        j = i
        counter = 0
        lista = []
        while j**3<10**(n+1):
            j += 1
            val2 = j**3
            if val2 < 10**n:
                continue
            if isPerm(val,val2):
                counter += 1
                lista.append(j)
                if counter == 4:
                    t1 = time()
                    print("Procedure took", t1-t0)
                    print(val)
                    exit("haleluyah!")
        if counter > maxval:
            maxval = counter
            print(i,maxval,lista)
