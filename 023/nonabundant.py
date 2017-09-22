from math import sqrt
from time import clock

def divisors(a):
    lista=[1]
    i = 1
    while i<int(sqrt(a)):
        i += 1
        if i in lista:
            break
        if a%i == 0:
            lista.append(i)
            if a//i != i:
                lista.append(a//i)
    return sorted(lista)

def isabundant(a):
    if sum(divisors(a)) > a:
        return True
    return False

bign=28123
biglist=[]

for i in range(bign+30):
    if isabundant(i):
        biglist.append(i)

dlugosc = len(biglist)-1

def abundantsum(nn):
    start = 0
    stop = dlugosc
    while stop-start > 5:
        if biglist[stop]>nn:
            stop = (stop-start)//2
        else:
            start = stop
            stop = 2*stop
    for i in range(stop):
        for j in range(stop,0,-1):
            if biglist[i] + biglist[j] == nn:
                return True
            if biglist[i] + biglist[j] < nn or biglist[i] > nn:
                break

finalsum = 0

t0 = clock()

for i in range(1,bign):
    if not abundantsum(i):
        finalsum += i
    if i%1000 == 0:
        t1 = clock()
        print(i,t1-t0)

print(finalsum)
