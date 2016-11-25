import math

def findtriplet(n):
    for a in range(1,n//2):
        for b in range(1,n//2):
            c = math.sqrt(a**2+b**2)
            if a+b+c==n:
                return n,[a,b,int(c)]
    return n,False

nn = 1001

for a in range(1000,nn):
    print(findtriplet(a))
    print(findtriplet(a)[1][0]*findtriplet(a)[1][1]*findtriplet(a)[1][2])
