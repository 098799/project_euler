from time import clock
from sympy import primefactors

###Simple brute force seems to work in 2-3 seconds:
def GeneratePF(nn):
    global BigList
    BigList = {}
    for i in range(2,nn+1):
        BigList[i] = set(primefactors(i))
    return BigList

def RelativelyPrimeInRange(nn,start,stop):
    suma = 0
    if nn%2 == 0:
        if start%2 == 0:
            start += 1
        for i in range(start,stop,2):
            if not BigList[i] & BigList[nn]:
                suma += 1
        return suma
    for i in range(start,stop):
        if not BigList[i] & BigList[nn]:
            suma += 1
    return suma

def BruteForce(nn):
    totalsum = 0
    for i in range(5,nn+1):
        start = i//3+1
        if i%2 == 0:
            stop = i//2
        else:
            stop = i//2+1
        totalsum += RelativelyPrimeInRange(i,start,stop)
    return totalsum

nnn = 12000

t0 = clock()
GeneratePF(nnn)
print(BruteForce(nnn))
t1 = clock()
print("Took",t1-t0)
