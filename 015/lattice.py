for n in range(21):

    path = [0] * 2*n

    final = 0

    for i in range(2**(2*n)):
        a = bin(i+2**(2*n))
        for j in range(1,2*n+1):
            path[j-1] = a[-j]
        sum = 0
        for j in range(2*n):        
            sum += int(path[j])
        if sum == n:
            final += 1
                    
    print(final)
