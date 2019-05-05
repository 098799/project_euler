from math import floor, sqrt
from itertools import count

def cf(n):
    a = floor(sqrt(n))
    az = a
    m = 0
    d = 1
    j = 0
    for i in count(1):
        m = d*a-m
        d = (n-m**2)/d
        a = floor((az + m)/d)
        j += 1
        if a == 2*az:
            return j

totalsum = 0
for i in range(10001):
    ii = sqrt(i)
    if ii != ii//1:
        if cf(i)%2 == 1:
            totalsum += 1

print(totalsum)
