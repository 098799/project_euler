import numpy as np
from math import floor
from mpmath import mp

biglist = []
for i in range(1, 101):
    val = np.sqrt(i)
    if floor(val) != val:
        biglist.append(i)

mp.dps = 110

totalsuma = 0
for j in biglist:
    suma = 0
    squareroot = str(mp.sqrt(j))
    for i in squareroot[0]+squareroot[2:101]:
        suma += int(i)
    print(j, squareroot, suma)
    totalsuma += suma

print(totalsuma)
