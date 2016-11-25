import math

i = 1

def checkprime(a):
    if a == 2:
        return True
    for i in range(2,math.ceil(math.sqrt(a))+1):
        if a%i == 0:
            return False
    return True

a = 600851475143

lista=[]

while a>1:
    i = i + 1
    if checkprime(i):
        if a%i == 0:
            lista.append(i)
            a = a//i
            i = i - 1

print(lista)
