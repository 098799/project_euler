nn = 10**6

num = 1
bot = 0
top = 3/7
for d in range(8,nn+1):
    for n in range(num,d):
        fr = n/d
        if fr<top:
            num = n
            if fr>bot:
                bot = fr
                numba = n
                demba = d
        else:
            break

print(numba,demba,bot,3/7)
