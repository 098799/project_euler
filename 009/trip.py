from math import sqrt

def findtriplet(n):
    for a in range(1,n//2):
        for b in range(a,n//2):
            c = sqrt(a**2+b**2)
            if a+b+c==n:
                return int(a*b*c)
    return n,False

a = 1000
print(findtriplet(a))
