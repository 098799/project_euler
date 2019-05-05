def SumCounter(nmax):
    results = {}
    for i in range(1,nmax):
        results[i] = 0
    for j in range(1,nmax):
        for i in range(1+j,nmax):
            if i/2<=j:
                results[i] += results[i-j]+1
            else:
                results[i] += results[i-j]
    return results[100]

print(SumCounter(101))
