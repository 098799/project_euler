import time

def nextcol(n):
    if n%2 == 0:
        n = n//2
    else:
        n = 3*n + 1
    return n

wartosci=[]
maxx=[0,0]

kiedyskonczyc = int(10**6)

t0 = time.clock()

for n in range(1,kiedyskonczyc):

    i  = 1
    nn = n

    while n > 1:
        n = nextcol(n)
        i += 1

    wartosci.append(i)
    if i>maxx[0]:
        maxx[0] = i
        maxx[1] = nn

#print(wartosci)

print(maxx)

print(time.clock()-t0)
