from math import ceil, sqrt

nn = 10**5

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

nnn = 10000

def check_things(i):
    if not genif(i):
        for j in biglist:
            if j > i:
                return False
            for k in range(1,int(sqrt(nnn))):
                test = j + 2*k**2 
                if i == test:
                    return True, j,"+ 2*",k,"^2"
                elif i < test:
                    break
        return False
    return "prime"

for i in range(3,nnn,2):
    print(i,check_things(i))
    if check_things(i) == False:
        print("Hooray",i)
        break
