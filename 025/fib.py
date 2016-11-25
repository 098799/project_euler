a = 1
b = 1
i = 1

condition = True
while condition:
    a, b = b, a + b
    i += 1
    if a//10**999 != 0:
        condition = False
        print(i,a)
