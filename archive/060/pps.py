from math import ceil, sqrt, floor
from sys import exit
from itertools import permutations, combinations
import time

nn = 10**8

t0 = time.clock()
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
t1 = time.clock()
print("Sieve took",t1-t0)

def genif(n):
    if biglist[n] == True:
        return True
    return False

def concatenate(n):
    return int(str(n[0]) + str(n[1]))

def check_set(n):
    le = len(n)
    for i in range(le):
        for j in range(i+1,le):
            ll = [n[i],n[j]]
            if not genif(concatenate(ll)):
                return False,"blabber"
            ll = [n[j],n[i]]
            if not genif(concatenate(ll)):
                return False,"blabber"
    return True,[n,sum(n)]

def find_concatenations(x,n):
    zbior = set()
    for i in range(n):
        prajm = fakelist[i]
        if genif(concatenate([x,prajm])):
            if genif(concatenate([prajm,x])):
                zbior.add(prajm)
    return zbior

ma = 1150
mb = 800

suma = 10**6
for k in range(mb):
    for l in range(k+1,mb):
        for m in range(l+1,mb):
            if check_set([fakelist[k],fakelist[l],fakelist[m]])[0]:
                aa = find_concatenations(fakelist[k],ma)
                bb = find_concatenations(fakelist[l],ma)
                cc = find_concatenations(fakelist[m],ma)
                res = aa & bb & cc
                dlugosc_wynikow = len(res)
                if dlugosc_wynikow > 1:
                    for i in res:
                        for j in res:
                            if genif(concatenate([i,j])) and genif(concatenate([j,i])):
                                total = sum([fakelist[k],fakelist[l],fakelist[m],i,j])
                                if total<suma:
                                    suma = total
                                    print(suma)
                                    t2 = time.clock()
                                    print("Looking took",t2-t1)
                                    exit("doot doot")


# for i in range(ma):
#     for j in range(i+1,ma):
#         for k in range(j+1,ma):
#             for l in range(k+1,ma):
#                 #for m in biglist[l+1:ma]:
#                     longer = [fakelist[l],fakelist[k],fakelist[j],fakelist[i]]#,fakelist[m]]
#                     result = check_set(longer)
#                     if result[0]:
#                         print(result[1])
#                         t2 = time.clock()
#                         print("Looking took",t2-t1)
#                         exit("doot doot")
