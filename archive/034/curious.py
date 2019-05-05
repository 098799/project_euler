from math import factorial as f

nn = 1000000

def find_breaker(i):
    crit = True
    j = 0
    while (crit):
        j += 1
        if 10**j>i:
            return  j
            crit = False

def dig(i):
    breaker = find_breaker(i)
    table = []
    for k in range(1,breaker+1):
        table.append((i%10**k)//10**(k-1))
    return table

largesum = 0
for n in range(3,nn):
    sum = 0
    for i in range(find_breaker(n)):
        sum += f(dig(n)[i])
    if sum == n:
        print(sum)
        largesum += sum

print(largesum)
