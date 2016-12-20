from math import floor, sqrt
from time import clock

###SIEVE FOR PRIME NUMBERS
nn = 2*10**6

t0 = clock()
def sieve(n):
    primes = [True for i in range(n)]
    primes[0] = False
    primes[1] = False
    for i in range(2,floor(sqrt(n))+1):
        if primes[i] == True:
            for j in range(i**2,n,i):
                primes[j] = False
    return primes

biglist = sieve(nn)
t1 = clock()
print("Sieve took",t1-t0)
###END OF SIEVE


suma = 0

for i in range(2,nn):
    if biglist[i]:
        suma = suma + i

print(suma)
