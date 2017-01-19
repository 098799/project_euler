from itertools import count
from copy import copy
from math import factorial
from collections import Counter

def step(n):
    val = sum(int(i)**2 for i in str(n))
    return val

lista1 = set()
lista89 = set()
lista1.add(1)
lista89.add(89)

totalsum = 0
for n in range(2,10**7):
    n = int(''.join(sorted(list(str(n)))))
    val = copy(n)
    for i in count(1):
        val = step(val)
        if val in lista1:
            lista1.add(val)
            break
        if val in lista89:
            lista89.add(val)
            totalsum += 1
            break

print(totalsum)
