from itertools import count
from math import sqrt, floor

def numofdiv(n):
    if n == 1:
        return 1
    suma = 0
    for i in range(2,floor(sqrt(n))):
        if n%i == 0:
            suma += 2
    return suma+2

suma = 0
for i in count(1):
    suma += i
    if numofdiv(suma)>=500:
        print(suma)
        break
