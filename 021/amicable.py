from math import sqrt


def properDivisor(n):
    lista = [1]
    if n > 1:
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                lista.append(i)
                if i != n/i:
                    lista.append(int(n/i))
    return lista


totalsum = 0

for i in range(2, 10001):
    val = sum(properDivisor(i))
    val2 = sum(properDivisor(val))
    if val2 == i and val != val2:
        totalsum += val+val2

print(int(totalsum/2))
