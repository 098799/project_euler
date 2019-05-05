import math

def checkprimeness(a):
    for i in range(2,int(math.sqrt(a))+1):
        if a%i == 0:
            return False
    return True

sum = 0
i = 1
lista=[]

while sum<10001:
    i += 1
    if checkprimeness(i):
        sum += 1
        lista.append(i)

print(lista[-1])
