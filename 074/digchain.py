from math import factorial
from time import clock
from itertools import combinations_with_replacement as cwr
from collections import Counter

def step(n):
    return sum(factorial(int(i)) for i in str(n))

def sixty(nn):
    n = 0
    if not isinstance(nn, int):
        for i, val in enumerate(nn):
            n += val*10**(len(nn)-1-i)
    else:
        n = nn
    zbior = {n}
    m = step(n)
    i = 1
    while True:
        if m in zbior:
            if i == 60:
                return True
            return False
        if i>60:
            return False
        zbior.add(m)
        i += 1
        m = step(m)

def BruteForce():
    t0 = clock()
    totalsum = 0
    for i in range(10**6+1):
        if sixty(i):
            totalsum += 1
            print(i)
    print(totalsum)
    t1 = clock()
    print("Took",t1-t0)
    #Takes about a minute

def SmartForce():
    t0 = clock()
    totalsum = 0
    for k in range(1,7):
        for i in cwr(range(9,-1,-1),k):
            if sixty(i):
                ctr = Counter(i)
                totalsum += permut(ctr)
    print(int(totalsum))
    t1 = clock()
    print("Took",t1-t0)
    #Takes half a second, but I couldn't be bothered to figure out what happens
    #if some number has more than one zero...

def permut(dicti):
    total = factorial(sum(dicti[i] for i in dicti))
    for i in dicti:
        total /= factorial(dicti[i])
    if 0 in dicti:
        total -= factorial(sum(dicti[i] for i in dicti)-1)
    return total

SmartForce()
