thelist=[20,19,18,17,16,15,14,13,12,11]

def checkthething(a):
    for i in thelist:
        if a%i != 0:
            return False
    return True

a=1
found=False
while not found:
    if checkthething(a):
        print(a)
        for i in range(len(thelist)):
            print(a/thelist[i])
        found=True
    a = a + 1
