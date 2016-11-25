lista=[]

with open('data','r') as f:
    full=f.read().splitlines()

fulminimul=[]

for i in range(len(full)):
    linen=full[i].split()
    fulminimul.append([])
    for j in range(len(linen)):
        a = linen[j]
        fulminimul[i].append(a)

prod = 0
for i in range(len(fulminimul[0])):
    for j in range(len(fulminimul[0])):
        fulminimul[i][j] = int(fulminimul[i][j])

for i in range(len(fulminimul[0])):
    for j in range(len(fulminimul[0])-3):
        ntemp = 1
        utemp = 1
        for k in range(4):
            ntemp *= fulminimul[i][j+k]
            utemp *= fulminimul[j+k][i]
        if ntemp > prod:
            prod = ntemp
        if utemp > prod:
            prod = utemp

for i in range(len(fulminimul[0])-3):
    for j in range(len(fulminimul[0])-3):
        dtemp = 1
        atemp = 1
        for k in range(4):
            dtemp *= fulminimul[i+k][j+k]
            atemp *= fulminimul[i+3-k][j+k]
        if dtemp > prod:
            prod = dtemp
        if atemp > prod:
            prod = atemp
        
print(prod)
