from itertools import count
from numpy import argmax
from time import clock

t0 = clock()

def collatz(n):
    if n%2 == 0:
        return int(n/2)
    return int(3*n+1)

bigtable = {1:1}

###Behold the power of recursive functions ffs!
def fill(bigtable,n):
    val = collatz(n)
    if val not in bigtable:
        fill(bigtable,val)
    bigtable[n] = bigtable[val]+1

nn = 10**6+1

for i in range(2,nn):
    fill(bigtable,i)

totalmax = 0
for i in range(2,nn):
    val = bigtable[i]
    if val>totalmax:
        totalmax = val
        arg = i

print(arg)

t1 = clock()
print("Stuff took",t1-t0)
### less than 5s so i guess improvement
