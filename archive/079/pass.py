from collections import Counter

with open("p079_keylog.txt") as infile:
    res = infile.read().split("\n")[:-1]

print(res)

    
kanter = Counter([i[0] for i in res])

print(kanter)

kanter = Counter([i[1] for i in res])

print(kanter)

kanter = Counter([i[2] for i in res])

print(kanter)




73162890
