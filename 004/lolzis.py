def ifpali(a):
    for i in range(0,len(str(a))//2):
        if str(a)[i] != str(a)[-(i+1)]:
            return False
    return True

lista=[]
beg=100
end=1000
for a in range(beg, end):
    for b in range(beg, end):
        if ifpali(a*b) == True and a*b not in lista:
            lista.append(a*b)

print(sorted(lista))
