from itertools import permutations as perm
from math import factorial as fac

def divizi(n,i):
    primes = (2,3,5,7,11,13,17)
    numba = n[i]*100+n[i+1]*10+n[i+2]
    if numba%primes[i-1]==0:
        return True
    else:
        return False

sum = 0

nn = 10
x = perm(range(nn))
for i in range(2*10**6): #fac(nn)):
    counter = 0
    iteration = next(x)
    for j in range(1,8):
        if divizi(iteration,j):
            counter += 1
    if counter == 7:
        string = ''
        for k in range(10):
            string = string + str(iteration[k])
        print(string)
        sum += int(string)

print(sum)
