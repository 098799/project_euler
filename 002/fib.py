a,b=1,2
sum=2
while b<4*10**6:
    a=a+b
    b=a+b
    if a%2 == 0:
        sum = sum + a
    elif b%2 == 0:
        sum = sum + b

print(sum)
