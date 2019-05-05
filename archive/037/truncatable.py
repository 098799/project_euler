from math import ceil,sqrt

nn = 10**3

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
    for i in range(7,int(ceil(sqrt(n)))):
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

def trun(n):
    en = str(n)
    for i in range(len(en)-1):
        temp1 = int(str(n)[i+1:])
        temp2 = int(str(n)[:-i-1])
        if not genif(temp1) or not genif(temp2):
            return False
    return True

sum = 0
for i in range(10,1000000):
    if genif(i):
        if trun(i):
            print(i)
            sum += i

print(sum)
