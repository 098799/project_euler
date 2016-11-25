import csv

with open('p042_words.txt') as inputfile:
    results = list(csv.reader(inputfile))[0]

valuej = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U':21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

trianglej = list(int(n*(n+1)/2) for n in range(22))

counter = 0

for j in results:
    temp = list(j)
    value = 0
    for i in temp:
        value += valuej[i]
    if value in trianglej:
        print(j,value)
        counter += 1

print(counter)
