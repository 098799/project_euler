def ifpali(a):
    for i in range(0,len(str(a))//2):
        if str(a)[i] != str(a)[-(i+1)]:
            return False
    return True

lista=[]
beg=100
end=1000
for a in range(beg, end):
    for b in range(a, end):
        if ifpali(a*b) == True:
            lista.append(a*b)

print(sorted(lista)[-1])
