from csv import reader

results = reader(open('data'))

suma = 0
for i in range(100):
    suma += int(next(results)[0])

print(str(suma)[:10])
