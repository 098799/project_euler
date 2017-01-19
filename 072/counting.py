from math import gcd, floor, sqrt
from time import clock
from sympy import primefactors
from itertools import combinations

# ###SIEVE FOR PRIME NUMBERS
# nn = 10**3

# t0 = clock()
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
# # fakelist=[]
# # for i in range(len(biglist)):
# #     if biglist[i]:
# #         fakelist.append(i)
# t1 = clock()
# print("Sieve took",t1-t0)
# ###END OF SIEVE

# nn = 500

# tablica = []

# for i in range(2,nn):
#         pf = primefactors(i)
#         partialsum = 0
#         for j in range(1,i):
#             if gcd(i,j) == 1:
#                 partialsum += 1
#         tablica.append(partialsum)

t0=clock()
def numberOfFractions(n):
    pf = primefactors(n)
    length = len(pf)
    suma = n-1
    for i in range(length):
        for j in combinations(pf,i+1):
            product = 1
            for k in j:
                product *= k
            suma += (-1)**(i+1) * (n/product-1)
    return int(suma)

totalsum = 0
for i in range(2,10**6 + 1):
    totalsum += numberOfFractions(i)

print(totalsum)
t1=clock()
print("My version took",t1-t0)

t0=clock()
def phi(n):
    phi = n
    for i in primefactors(n):
        phi *= (1-1/i)
    return int(phi)

print(sum(phi(i) for i in range(2,10**6+1)))

t1=clock()
print("Totient took",t1-t0)

print("Cool, quite similar actually!")
