stringu = "0"
i = 0

while len(stringu) < 10**7:
    i += 1
    stringu += str(i)

product = 1
for i in range(0,7):
    product *= int(stringu[10**i])

print(product)
