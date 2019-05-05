from math import sqrt
from itertools import permutations

def tria(n):
    return int(n*(n+1)/2)

def squa(n):
    return int(n**2)

def pent(n):
    return int(n*(3*n-1)/2)

def hexa(n):
    return int(n*(2*n-1))

def hept(n):
    return int(n*(5*n-3)/2)

def octa(n):
    return int(n*(3*n-2))

def revtria(p):
    return 1/2*(sqrt(1+8*p)-1)

def revsqua(p):
    return sqrt(p)

def revpent(p):
    return 1/6*(1+sqrt(1+24*p))

def revhexa(p):
    return 1/4*(1+sqrt(1+8*p))

def revhept(p):
    return 1/10*(3+sqrt(9+40*p))

def revocta(p):
    return 1/3*(1+sqrt(1+3*p))

def checker(x,n):
    if n == 3:
        lol = revtria(x)
    elif n == 4:
        lol = revsqua(x)
    elif n == 5:
        lol = revpent(x)
    elif n == 6:
        lol = revhexa(x)
    elif n == 7:
        lol = revhept(x)
    elif n == 8:
        lol = revocta(x)
    if lol == lol//1:
        return True
    return False

for co in permutations([3,4,5,6,7,8]):

    for i in range(10,100):
        for j in range(10,100):
            a = int(str(i)+str(j))
            if checker(a,co[0]):
                for k in range(10,100):
                    b = int(str(j)+str(k))
                    if checker(b,co[1]):
                        for l in range(10,100):
                            c = int(str(k)+str(l))
                            if checker(c,co[2]):
                                for m in range(10,100):
                                    d = int(str(l)+str(m))
                                    if checker(d,co[3]):
                                        for n in range(10,100):
                                            e = int(str(m)+str(n))
                                            f = int(str(n)+str(i))
                                            if checker(e,co[4]) and checker(f,co[5]):
                                                print(sum([a,b,c,d,e,f]))
