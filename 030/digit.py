n = 5

def search(a):
    suma = 0
    aa = str(a)
    for i in range(len(aa)):
        suma += int(aa[i])**n
    return suma

prod = 0

for i in range(2,10000000):
    if search(i) == i:
        prod += i

print(prod)
