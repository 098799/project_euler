from math import floor, sqrt, exp
from itertools import count
from fractions import Fraction
import numpy as np
from sys import exit

def ann(n):
    if n == 1:
        return 2
    if (n-1)%3 == 1 or (n-1)%3 == 0:
        return 1
    if (n-1)%3 == 2:
        return int(n/3*2)

def eapprox(n):
    if n == 1: return (2,1)
    num = ann(n)
    den = 1
    for i in range(n,1,-1):
        (num,den) = (den,num)
        num += ann(i-1)*den
    return num,den



for i in range(1,101):
    val = eapprox(i)
    print(i,sum(int(j) for j in str(val[0])))

#print(Fraction(2+1/(1+1/2)).limit_denominator())
