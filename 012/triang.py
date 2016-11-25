def numofdiv(a):
    num = 0
    fin = a
    j = 0
    while fin > j:
        j += 1
        if a%j == 0:
            fin = a//j
            num += 1
    return (num-1)*2

going = True
i = 0
triangular = 0

while going:
    i += 1
    triangular += i
    if numofdiv(triangular) > 500:
        going = False
        print(triangular)
