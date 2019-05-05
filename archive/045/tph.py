def trian(n):
    return int(n*(n+1)/2)

def penta(n):
    return int(n*(3*n-1)/2)

def heksa(n):
    return int(n*(2*n-1))

maxp = 1
maxh = 1
for i in range(2,10**8):
    testt = trian(i)
    testing_penta = True
    testing_heksa = False
    while testing_penta:
        testp = penta(maxp)
        if testt == testp:
            testing_heksa = True
            testing_penta = False
        elif testp < testt:
            maxp += 1
        else:
            maxp -= 1
            testing_penta = False
    while testing_heksa:
        testh = heksa(maxh)
        if testt == testh:
            print("Next found",i,testt,maxp,testp,maxh,testh)
            testing_heksa = False
        elif testh < testt:
            maxh += 1
        else:
            maxh -= 1
            testing_heksa = False

