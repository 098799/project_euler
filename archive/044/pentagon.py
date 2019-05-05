from math import sqrt, floor

def pentagon(n):
    return int(n*(3*n-1)/2)

def check_pentagon(n):
    pn = 1/6*(1+sqrt(1+24*n))
    if pn==int(floor(pn)):
        return True
    return False

ni = 2
nn = 3000

for i in range(ni,nn):
    for j in range(i,nn):
        pi = pentagon(i)
        pj = pentagon(j)
        if check_pentagon(pj-pi):
            if check_pentagon(pi+pj):
                print(i,j,pentagon(j)-pentagon(i))
