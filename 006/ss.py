def sumsq(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**2
    return sum

def sqsum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum**2

n = 100
print(sqsum(n)-sumsq(n))
