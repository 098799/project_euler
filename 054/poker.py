import csv

def val(n):
    global values
    vac = []
    for i in range(5):
        vac.append(values[n[i][0]])
    return vac

def psort(n):
    global values
    en = sorted(n)
    zmiana = 1
    while zmiana>0:
        zmiana = 0
        for i in range(4,0,-1):
            if values[en[i][0]]<values[en[i-1][0]]:
                temp = en[i-1]
                en[i-1] = en[i]
                en[i] = temp
                zmiana += 1
    return en

def straight_flush(n):
    global values
    if flush(n)[0] and straight(n)[0]:
        return True,values[n[4][0]]
    return False,"giberish"

def four(n):
    v = val(n)
    if v[0] == v[1] == v[2] == v[3]:
        return True,v[0],v[4]
    if v[1] == v[2] == v[3] == v[4]:
        return True,v[1],v[0]
    return False,"giberish"

def fh(n):
    v = val(n)
    if v[0] == v[1] == v[2] and v[3] == v[4]:
        return True,v[0],v[3]
    if v[2] == v[3] == v[4] and v[0] == v[1]:
        return True,v[2],v[0]
    return False,"giberish"

def flush(n):
    global values
    v = val(n)
    if n[0][1] == n[1][1]== n[2][1] == n[3][1] == n[4][1]:
        return True,v[4],v[3],v[2],v[1],v[0]
    return False,"giberish"

def straight(n):
    v = val(n)
    if v[0] == v[1]-1 == v[2]-2 == v[3]-3 == v[4]-4:
        return True,v[4]
    return False,"giberish"

def four(n):
    v = val(n)
    if v[0] == v[1] == v[2] == v[3]:
        return True,v[0],v[4]
    if v[1] == v[2] == v[3] == v[4]:
        return True,v[1],v[0]
    return False,"giberish"

def three(n):
    v = val(n)
    if v[0] == v[1] == v[2]:
        return True,v[0],v[4],v[3]
    if v[1] == v[2] == v[3]:
        return True,v[1],v[4],v[0]
    if v[2] == v[3] == v[4]:
        return True,v[2],v[1],v[0]
    return False,"giberish"

def twopair(n):
    v = val(n)
    if v[0] == v[1] and v[2] == v[3]:
        return True,v[2],v[0],v[4]
    if v[0] == v[1] and v[3] == v[4]:
        return True,v[3],v[0],v[2]
    if v[1] == v[2] and v[3] == v[4]:
        return True,v[3],v[1],v[0]
    return False,"giberish"

def onepair(n):
    v = val(n)
    if v[0] == v[1]:
        return True,v[0],v[4],v[3],v[2]
    if v[1] == v[2]:
        return True,v[1],v[4],v[3],v[0]
    if v[2] == v[3]:
        return True,v[2],v[4],v[1],v[0]
    if v[3] == v[4]:
        return True,v[3],v[2],v[1],v[0]
    return False,"giberish"

def rank(n):
    if straight_flush(n)[0]:
        return 9,straight_flush(n)[1:]
    if four(n)[0]:
        return 8,four(n)[1:]
    if fh(n)[0]:
        return 7,fh(n)[1:]
    if flush(n)[0]:
        return 6,flush(n)[1:]
    if straight(n)[0]:
        return 5,straight(n)[1:]
    if three(n)[0]:
        return 4,three(n)[1:]
    if twopair(n)[0]:
        return 3,twopair(n)[1:]
    if onepair(n)[0]:
        return 2,onepair(n)[1:]
    else:
        return 1,[val(n)[4],val(n)[3],val(n)[2],val(n)[1],val(n)[0]]

filee = open("p054_poker.txt")
hands = csv.reader(filee)

values = {'A': 4,'K': 3,'Q': 2,'J': 1,'T': 0, '9': -1, '8': -2, '7': -3, '6': -4, '5': -5, '4': -6, '3': -7, '2': -8}

totalsum = 0

for i in range(1000):
    hand = next(hands)
    hand1 = hand[0:5]
    hand2 = hand[5:10]
    hand1 = psort(hand1)
    hand2 = psort(hand2)
    r1 = rank(hand1)
    r2 = rank(hand2)

    if r1[0]>r2[0]:
        totalsum += 1
    elif r1[0] == r2[0]:
        for i in range(len(r1[1])):
            if r1[1][i]>r2[1][i]:
                totalsum += 1
                break
            elif r1[1][i]<r2[1][i]:
                break

print(" ",totalsum)

