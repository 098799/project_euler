import math

def checkprime(a):
    if a<2:
        return False
    if a == 2:
        return True
    for i in range(2,math.ceil(math.sqrt(a))+1):
        if a%i == 0:
            return False
    return True

def formula(n,a,b):
    return n**2 + a*n + b

maxy = [0,0,0]

for a in range(-1001,1001):
    for b in range(-1001,1001):
        suma = 0
        i = 0
        while True:
            i += 1
            if checkprime(formula(i,a,b)):
                suma += 1
            else:
                break
        if suma > maxy[2]:
            maxy = [a,b,suma]

print(maxy,maxy[0]*maxy[1])
