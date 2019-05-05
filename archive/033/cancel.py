n = 100
counter = 0
cco = 0

def cg1(i):
    return i//10

def cg2(i):
    return i%10

nom = 1
denom = 1

for i in range(10,n):
    for j in range(10,i):
        if (cg2(j) == cg1(i)):
            if (cg1(j) != 0 and cg2(i) != 0):
                if (j/i==cg1(j)/cg2(i)):
                    print(j,i)
                    nom = nom * j
                    denom = denom * i

print(nom,denom)
