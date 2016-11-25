denominaly=[200,100,50,20,10,5,2,1]

# def rozmien(a):
#     cont = 0
#     if a == 0:
#         cont += 1
#     if a == 1:
#         reszta = a - 1
#         rozmien(reszta)
#     if a > 1:
#         for i in range(len(denominaly)):
#             if a >= denominaly[i]:
#                 reszta = a - denominaly[i]
#                 rozmien(reszta)
#     return cont
    
# for i in range(0,10):
#     print(i,rozmien(i))

def rz(a):
     lista = []
     i = 0
     if a == 1:
         lista.append(1)
         return lista
     while a>0:
         if denominaly[i] <= a:
             a = a - denominaly[i]
             lista.append(denominaly[i])
         else:
             i = i+1
         if a == 1:
             lista.append(1)
             return lista
     return lista

def rw(a):
    lista = []
    i = 0
    if a == 1:
        lista.append(1)
        return lista
    while a>0:
        if denominaly[i] < a:
            a = a - denominaly[i]
            lista.append(denominaly[i])
        else:
            i = i+1
        if a == 1:
            lista.append(1)
            return lista
    return lista

duzalista=[0]*30
con=0

for i in range(5,6):
    duzalista[con]=rz(i)
    con += 1
    for j in rz(i):
        duzalista[con] = [rw(j)]
        con += 1
        counter = False
        for k in rw(j):
            if k != 1 and counter == False:
                duzalista[con] = [rw(k)]
                con += 1
                counter = True
            else:
                duzalista[con-1].append([k])
            

print(duzalista)
