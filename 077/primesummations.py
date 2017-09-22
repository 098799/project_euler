from math import floor, sqrt

###SIEVE FOR PRIME NUMBERS
nn = 10**3

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
fakelist=[]
for i in range(len(biglist)):
    if biglist[i]:
        fakelist.append(i)
###END OF SIEVE


def SumCounter(nmax):
    results = {}
    for i in range(2,nmax):
        results[i] = 0
    for j in fakelist:
        for i in range(2+j,nmax):
            if i/2<=j:
                results[i] += results[i-j]+1
            else:
                results[i] += results[i-j]
    return results

print(SumCounter(101))
