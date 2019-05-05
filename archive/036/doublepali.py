def cpdec(n):
    en = str(n)
    # still = True
    # while still:
    #     if en[-1] == "0":
    #         en = en[:-1]
    #     else:
    #         still = False
    l  = len(en)
    if l%2 == 0:
        le = int(l/2)
    else:
        le = int((l-1)/2)
    for i in range(le):
        if en[i] != en[-(i+1)]:
            return False
    return True

def cpbin(i):
    en = str(bin(i))[2:]
    # still = True
    # while still:
    #     if en[-1] == "0":
    #         en = en[:-1]
    #     else:
    #         still = False
    l  = len(en)
    if l%2 == 0:
        le = int(l/2)
    else:
        le = int((l-1)/2)
    for i in range(le):
        if en[i] != en[-(i+1)]:
            return False
    return True

sum = 0
for i in range(1,10**9,2):
    if cpdec(i):
        if cpbin(i):
            print(i,bin(i))
            sum += i

print(sum)
