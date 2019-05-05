f = open('data','r')
lista = []
for lines in f:
    lista.append(lines)
    
sum = [0]*60

for i in range(50):
    suma = 0
    for j in range(100):
        suma += int(lista[j][49-i])
    for k in range(3,-1,-1):
        sum[i+k] += suma//(10**k)%10
        if sum[i+k] > 9:
            sum[i+k+1] += 1
            sum[i+k] += -10

print(sum)
