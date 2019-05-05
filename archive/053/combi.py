from math import factorial

def binom(n,r):
    binom = 1
    for i in range(n,n-r,-1):
        binom = binom * i
    binom = binom/factorial(r)
    return binom

suma = 0
for n in range(101):
    value = 1
    i = 0
    for i in range(1,n+1):
        value = binom(n,i)
        if value > 1e6:
            suma += n-2*i+1
            break
    print(" ",suma)
