from csv import reader

naszalista = list(range(32,35)) + list(range(39,65)) + list(range(65,91)) + list(range(97,123))
library = {i:chr(i) for i in naszalista}
antilibrary = {library[i]:i for i in naszalista}

filee = open("p059_cipher.txt")

results = list(reader(filee))[0]

totalsum = 0

for a in range(97,123):
    for b in range(97,123):
        for c in range(97,123):
            passwd = [a,b,c]
            trigger = False
            stringu = ''
            for i in range(len(results)):
                try:
                    stringu += library[int(results[i])^passwd[i%3]]
                except:
                    trigger = True
                    break
            if not trigger:
                print(stringu)
                for j in stringu:
                    totalsum += antilibrary[j]

print(totalsum)
