from math import floor, sqrt
from itertools import count

def giveFraction(n):
    a = floor(sqrt(n))
    az = a
    m = 0
    d = 1
    tablica = [a]
    for i in count(1):
        m = d*a-m
        d = (n-m**2)/d
        a = floor((az + m)/d)
        tablica.append(a)
        if a == 2*az:
            return tablica

def fromContinuedFraction(n,howmany):
    a = giveFraction(n)
    length = len(a)-1
    nom = [1,a[0]]
    den = [0,1]
    for i in range(2,howmany):
        nom.append(nom[-1]*a[(i-2)%length+1]+nom[-2])
        den.append(den[-1]*a[(i-2)%length+1]+den[-2])
    return [nom[1::],den[1::]]

def findX(D):
    nn=100
    nd = fromContinuedFraction(D,nn)
    for i in range(nn-1):
        if nd[0][i]**2 == 1+D*nd[1][i]**2:
            return nd[0][i]

totalmax = 0
for i in range(2,1000):
    if sqrt(i)//1 != sqrt(i):
        temp = findX(i)
        if temp>totalmax:
            totalmax = temp
            valtotalmax = i

print(valtotalmax)
