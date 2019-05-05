import collections

def isnt_doublet(n):
    en = str(n)
    res = collections.Counter(en)
    for i in res:
        if res[str(i)] > 1:
            return False
    return True

def is_pandigi(n):
    en = str(n)
    stringu = en
    if isnt_doublet(n):
        checker = True
        i = 1
        while checker:
            i += 1
            stringu += str(i*n)
            if not isnt_doublet(int(stringu)):
                return False,stringu
            if len(stringu) == 9:
                if isnt_doublet(stringu):
                    return True,stringu
                else:
                    return False,stringu
            elif len(stringu) > 9:
                return False,stringu
    else:
        return False,stringu

record = 0
for i in range(1,10000):
    lolex = is_pandigi(i)
    if lolex[0]:
        if int(lolex[1]) > record:
            record = int(lolex[1])
            print(i,record)
