biggest = 0

for a in range(100):
    for b in range(100):
        en = str(a**b)
        sum = 0
        for i in en:
            sum += int(i)
        if sum>biggest:
            biggest = sum

print(biggest)

