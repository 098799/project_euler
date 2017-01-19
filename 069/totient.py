from math import ceil, sqrt, floor, gcd
from sys import exit
from itertools import permutations, combinations
import time
from sympy import primefactors

##############################
# Comments:
# So it seems that my Sieve of Erathostenes and three methods of getting
# prime factors are slow as fuck. Thankfully sympy to the rescue and
# using a built in function for prime factorization. Although it feels
# a little bit like cheating...
##############################


### SIEVE FOR PRIME NUMBERS
# nn = 1*10**6

# t0 = time.clock()
# def sieve(n):
#     primes = [True for i in range(n)]
#     primes[0] = False
#     primes[1] = False
#     for i in range(2,floor(sqrt(n))+1):
#         if primes[i] == True:
#             for j in range(i**2,n,i):
#                 primes[j] = False
#     return primes

# biglist = sieve(nn)
# fakelist=[]
# for i in range(len(biglist)):
#     if biglist[i]:
#         fakelist.append(i)
# t1 = time.clock()
# print("Sieve took",t1-t0)
### END OF SIEVE

### (spurious) GET PRIME FACTORS -- METHOD 1
# def primeFactorBasedOnLists(n):
#     lista = []
#     for i in fakelist:
#         if n == 1:
#             return lista
#         while n%i == 0:
#             n = n/i
#             if i not in lista:
#                 lista.append(i)
#     return False

# factors = [[],[]]
# nn = 10**5
# t0 = time.clock()
# for i in range(2,nn):
#     factors.append(primeFactorBasedOnTuples(i))
# t1 = time.clock()
# print("Factoring took",t1-t0)

# def relativelyPrimeBasedOnLists(n,m):
#     if n == 1 or m == 1:
#         return True
#     for i in factors[n]:
#         for j in factors[m]:
#             if j == i:
#                 return False
#             elif j>i:
#                 break
#     return True
### EDN OF GET PRIME FACTORS -- METHOD 1

### (spurious) GET REALTIVELY PRIME -- METHOD 2 (built in function)
# def relativelyPrimeBasedOnGCD(n,m):
#     return gcd(n,m) == 1
### END

### (spurious) GET PRIME FACTORS -- METHOD 3 (sets)
# def relativelyPrimeBasedOnSets(n,m):
#     if n == 1 or m == 1:
#         return True
#     if factors[n].intersection(factors[m]) == set():
#         return True
#     return False

# ### FACTORING
# factors = [[],[]]

# nn = 10**5

# t0 = time.clock()
# for i in range(2,nn):
#     factors.append(primeFactorBasedOnSets(i))
# t1 = time.clock()
# print("Factoring took",t1-t0)
# ###END OF FACTORING

# t0 = time.clock()
# totalmax = 0
# for i in range(2,nn):
#     total = 0
#     for j in range(1,i):
#         if relativelyPrimeBasedOnGCD(j,i):
#             total += 1
#     noverphi = i/total
#     if noverphi > totalmax:
#         totalmax = noverphi
#         counter = i
#         print(counter)
# t1 = time.clock()
# print("Computing phi took",t1-t0)
### END

### CALCULATING PHI BASED ON NORMAL ALGORITHM
# t0 = time.clock()
# totalmax = 0
# for i in range(2,nn):
#     total = 0
#     for j in range(1,i):
#         if relativelyPrimeBasedOnGCD(j,i):
#             total += 1
#     noverphi = i/total
#     if noverphi > totalmax:
#         totalmax = noverphi
#         counter = i
#         print(counter)
# t1 = time.clock()
# print("Computing phi took",t1-t0)
### END




# def primeFactorBasedOnLists(n):
#     lista = []
#     for i in fakelist:
#         if n == 1:
#             return lista
#         while n%i == 0:
#             n = n/i
#             if i not in lista:
#                 lista.append(i)
#     return False
# factors = [[],[]]
# nn = 10**6
# t0 = time.clock()
# for i in range(2,nn):
#     factors.append(primeFactorBasedOnLists(i))
# t1 = time.clock()
# print("Factoring took",t1-t0)
### nice but still takes too long

def phi(n):
    phi = n
    for i in primefactors(n):
        phi *= (1-1/i)
    return int(phi)

totalmax = 0
counter = 0
for i in range(2,nn):
    val = i/phi(i)
    if val>totalmax:
        totalmax = val
        counter = i
        print(counter)
