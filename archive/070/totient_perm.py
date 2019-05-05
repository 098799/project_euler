from sympy import primefactors
from time import clock
from collections import Counter

def phi(n):
    phi = n
    for i in primefactors(n):
        phi *= (1-1/i)
    return int(phi)

def isPerm(n,m):
    en = Counter(list(str(n)))
    em = Counter(list(str(m)))
    if en == em: return True
    return False

nn = 10**7

totalmax = 10
t0 = clock()
for i in range(2,nn):
    j = phi(i)
    val = i/j
    if val<totalmax:
        if isPerm(j,i):
            totalmax = val
            print(i,val)
t1 = clock()
print("phi took",t1-t0)
### brute force like this should less than 8 minutes
