import math

def checkprime(a):
    if a == 2:
        return True
    for i in range(2,math.ceil(math.sqrt(a))+1):
        if a%i == 0:
            return False
    return True

def frac(a,how):
    return str(10**how//a)

def recur(a,how):
    for i in range(1,how):
        if frac(a,how)[i] == frac(a,how)[0]:
            count=0
            for j in range(1,100):
                if frac(a,how)[i+j] == frac(a,how)[0+j]:
                    count += 1
            if count == 99:
                return [i,frac(a,how)[0:i]]
    return False

nn=10000
maxy=0

for i in range(7,1000):
    if checkprime(i):
        a = recur(i,nn)
        print(i,a)
        if a[0]>maxy:
            maxy = a[0]

print(maxy)
