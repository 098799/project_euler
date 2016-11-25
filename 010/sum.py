import math

def checkprimeness(a):
    for i in range(2,int(math.sqrt(a))+1):
        if a%i == 0:
            return False
    return True

fin = 2*10**6

sum = 0

for i in range(2,fin):
    if checkprimeness(i):
        sum = sum + i

print(sum)
