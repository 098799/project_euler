from math import ceil, sqrt

nn = 10000

def easyif(n):
    if n == 1:
        return False
    if n in (2,3,5):
        return True
    if n%2 == 0:
        return False
    if n%3 == 0:
        return False
    if n%5 == 0:
        return False
    for i in range(7,int(ceil(sqrt(n)+1))):
        if n%i == 0:
            return False
    return True

biglist=[]
for i in range(2,nn):
    if easyif(i):
        biglist.append(i)

def hardif(n):
    for i in biglist:
        if n%i == 0:
            return False
    return True

def genif(n):
    global nn
    if n<nn:
        return easyif(n)
    else:
        return hardif(n)

for k in range(500,1200):
    for j in range(1000):
        sum = 0
        for i in biglist[j:j+k]:
            sum += i
        if sum>10**6:
            break
        if genif(sum):
            print(sum,k)
