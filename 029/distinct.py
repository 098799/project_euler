def gener(a,b):
    lista=[]
    for i in range(2,a+1):
        for j in range(2,b+1):
            k = i**j
            if k not in lista:
                lista.append(k)
    return lista

print(len(gener(100,100)))
