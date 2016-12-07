from math import sqrt, floor
from fractions import Fraction

def continued_fraction(n):
    x = 2
    for i in range(n):
        x = 2+Fraction(1,x)
    return 1+Fraction(1,x)

totalsum = 0

for i in range(10**3):
    a = continued_fraction(i)
    if len(str(a.numerator))>len(str(a.denominator)):
        totalsum += 1

print(totalsum)
