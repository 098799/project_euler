from math import sqrt, floor

def diag(n):
    lista = []
    counter = 1
    j = 0
    while True:
        j += 1
        for i in range(1,5):
            lista.append(counter)
            counter = counter + 2*j
            if counter>n:
                return lista

def sieve(n):
    primes = [True for i in range(n)]
    primes[0] = False
    primes[1] = False
    for i in range(2,floor(sqrt(n))+1):
        if primes[i] == True:
            for j in range(i**2,n,i):
                primes[j] = False
    return primes

n = 30000
biglist = sieve(n**2+1)
diagona = diag(n**2)

m = 25000
while True:
    m +=1
    suma = 0
    dlugosc = 1+4*(m-1)/2
    for i in range(1,int(dlugosc)):
        if biglist[diagona[i]] == True:
            suma += 1
    if m%10**3 == 0:
        print(m,suma/dlugosc)
    if(suma/dlugosc<0.1):
        print(m)
        break
