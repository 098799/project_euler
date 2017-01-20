def CheckRightness(c,a,b):
    if a**2 + b**2 == c**2:
        return True
    return False

def CheckAll(n):
    total = 0
    for i in range(3,n//2+1):
        for j in range(2,(n-i)//2):
            k = n-i-j
            if CheckRightness(i,j,k):
                print(n,i,j,k)
                total += 1
                if total > 1:
                    return False
    if total == 1:
        return True

totalsum = 0
for i in range(6,50):
    if CheckAll(i):
        totalsum += 1
print(totalsum)
