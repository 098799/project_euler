from itertools import count
from sys import exit

totalsum = 0

for n in range(1,100):
    for i in count(1):
        val = i**n
        dlugosc = len(str(val))
        if dlugosc == n:
            print(i,n,val)
            totalsum += 1
        if dlugosc > n:
            break

print(totalsum,"total")
