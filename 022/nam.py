# f = open('p022_names.txt','r')
# full=f.read().split('","')
# full[0] = full[0][1:]
# full[-1] = full[-1][:-1]

# xxx = open('x.dat','w')
# for i in range(len(full)):
#     xxx.write(full[i])
#     xxx.write("\n")

# sfull = sorted(full)

ff = open('sortnames.txt','r')
sfull = ff.read().splitlines()

alphabet = [ 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]

def val(a):
    return alphabet.index(str(a))+1

def alpval(a):
    sum = 0
    for i in range(len(a)):
        sum += val(a[i])
    return sum

sum = 0

for i in range(len(sfull)):
    sum += (i+1)*alpval(sfull[i])
    print(sfull[i],i+1,alpval(sfull[i]))

print(sum)
