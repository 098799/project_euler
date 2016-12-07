def make_reverse(n):
    en = str(n)
    stringu = ''
    for i in range(len(en)-1,-1,-1):
        stringu += en[i]
    return int(stringu)

def check_palindrome(n):
    en = str(n)
    length = len(en)
    for i in range(int(length/2)):
        if en[i] != en[length-i-1]:
            return False
    return True

def check_Lychrel(n):
    n += make_reverse(n)
    for i in range(30):
        if not check_palindrome(n):
            n += make_reverse(n)
        else:
            return False
    return True

totalsum = 0
for i in range(10,10**4):
    if check_Lychrel(i):
        totalsum += 1

print(" ",totalsum)
