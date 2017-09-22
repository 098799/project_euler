from sys import exit

def CheckRightness(c, a, b):
    if a + b == c:
        return True
    return False


def CheckAll(n):
    total = 0
    ctr = 0
    start=GenerateStartForI(n)
    stop=GenerateStopForI(n)
    print(n,start,stop)
    for i in range(start,stop,-1):
        isq = i**2
        counter = ctr
        ctr = 0
        for j in range(i-1,(n-i)//2,-1):
            ctr += 1
            jsq = j**2
            k = n-i-j
            ksq = k**2
            print(n, i, j, k, isq, jsq+ksq)
            if jsq+ksq<isq:
                break
            if j ==  (n-i)//2+1 and jsq+ksq>isq:
                if total == 1:
                    return True
                else:
                    return False
            if CheckRightness(isq,jsq,ksq):
                # print(n, i, j, k)
                total += 1
                if total > 1:
                    return False
    if total == 1:
        return True

def GenerateStartForI(n):
    for i in range(n//2-1,n//3,-1):
        if (i-1)**2+(n-i-i-1)**2>i**2:
            return i-1
    return n//2

def GenerateStopForI(n):
    for i in range(n//2-1,n//3,-1):
        j = (n-i)//2+1
        if j**2+(n-i-j)**2>i**2:
            return i
    return n//3

L = 50
totalsum = 0
for i in range(11,50):
    if CheckAll(i):
        totalsum += 1
print(totalsum)
