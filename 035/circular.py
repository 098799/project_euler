from math import ceil,sqrt

ltej = 6

nn = 10**3

def easyif(n):
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

def dissipate(n):
    table = []
    for i in range(len(str(n))):
        table.append(int(str(n)[i]))
    return table

def rotate(n,ile):
    table = []
    trial = dissipate(n)
    for i in range(1,ile+1):
        table.append(trial[-(ile+1)+i])
    for i in trial:
        table.append(i)
    for i in range(1,ile+1):
        del table[-1]
    return table

def merge(n):
    sum = 0
    counter = 0
    for i in n:
        sum += i*10**(len(n)-counter-1)
        counter += 1
    return sum

list = []

for i in range(2,10**6):
    if easyif(i):
        checker = True
        for j in range(1,len(str(i))):
            rot = merge(rotate(i,j))
            if not easyif(rot):
                checker = False
        if checker == True:
            list.append(i)

print(list)
print(len(list))
