from csv import reader

results = reader(open("p067_triangle.txt"), delimiter=' ')

res = list(results)

nn = 100

for i in range(nn-2,-1,-1):
    for j in range(i+1):
        l,r = int(res[i+1][j]),int(res[i+1][j+1])
        if l>r:
            res[i][j] = int(res[i][j]) + l
        else:
            res[i][j] = int(res[i][j]) + r

print(res[0][0])
