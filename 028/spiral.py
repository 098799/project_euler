import sys

def sqr(n):
   return (2*n-1)**2

n=502

lista=[[0,0],[1,1]]

for j in range(2,n):
    suma = lista[j-1][1]
    for i in range(1,5):
        suma += sqr(j-1)+(2*j-2)*i
    lista.append([j,suma])

print(lista)
