def check_right(i,j,k):
    if i**2 + j**2 == k**2:
        return True
    return False

def how_many(n):
    howmany = 0
    for i in range(1,n):
        for j in range(i,n-i):
            k = n-i-j
            if check_right(i,j,k):
                howmany += 1
    return howmany

top = 0
for i in range(5,1000):
    if i%60 == 0:
        if how_many(i) > top:
            top = how_many(i)
            print(i,top)
