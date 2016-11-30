def checkit(n):
    en = []
    for i in n:
        en.append(sorted(list(str(i))))
        for i in range(len(en)-1):
            if en[i] != en[i+1]:
                return False
    return True

for i in range(1,10**6):
    if checkit([i,2*i,3*i,4*i,5*i,6*i]):
        print([i,2*i,3*i,4*i,5*i,6*i])
