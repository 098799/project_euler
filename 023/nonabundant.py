from math import sqrt

def divisors(a):
    lista=[1]
    i = 1
    while i<int(sqrt(a)):
        i += 1
        if i in lista:
            break
        if a%i == 0:
            lista.append(i)
            if a//i != i:
                lista.append(a//i)
    return sorted(lista)

def isabundant(a):
    sum = 0
    for i in range(len(divisors(a))):
        sum += divisors(a)[i]
    if sum > a:
        return True
    else:
        return False

bign=28123
biglist=[]

for i in range(1,bign):
    if isabundant(i):
        biglist.append(i)

bbiglist=[]

k=0
for i in range(len(biglist)):
    for j in range(len(biglist)):
        k = k+1
        bbiglist.append(biglist[i]+biglist[j])

finalsum = 0

for i in range(bign):
    if i not in bbiglist:
        finalsum += i

print(finalsum)
