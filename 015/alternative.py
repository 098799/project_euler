pascal = [[1],[1,1]]

n = 40

for i in range(2,n+1):
    l = [1]
    for j in range(i-1):
        l.append(pascal[i-1][j]+pascal[i-1][j+1])
    l.append(1)
    pascal.append(l)

print(pascal[-1][n//2])
