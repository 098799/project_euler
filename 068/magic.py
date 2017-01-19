from sys import exit

### SMALLER VERSION IN COMMENTS
# stopwatch = False
# for a in range(4,0,-1):
#     numberb = list(range(a+1,7))
#     numberi = list(range(1,a))
#     if stopwatch:
#         exit()
#     for b in numberb:
#         tnumberb = numberb[:]
#         tnumberb.remove(b)
#         for c in tnumberb:
#             ttnumberb = tnumberb[:]
#             ttnumberb.remove(c)
#             for ii in ttnumberb:
#                 numberi.append(ii)
#             for i in numberi:
#                 tnumberi = numberi[:]
#                 tnumberi.remove(i)
#                 for j in tnumberi:
#                     ttnumberi = tnumberi[:]
#                     ttnumberi.remove(j)
#                     if b+j == c+i:
#                         for k in ttnumberi:
#                             if a+i == b+k:
#                                 stopwatch = True
#                                 res = int(str(a)+str(i)+str(j)+str(b)+str(j)+str(k)+str(c)+str(k)+str(i))
#                                 print(res)

stopwatch = False
for a in range(6,0,-1):
    numberb = list(range(a+1,11))
    numberi = list(range(1,a))
    if stopwatch:
        exit()
    for b in numberb:
        tnumberb = numberb[:]
        tnumberb.remove(b)
        for c in tnumberb:
            ttnumberb = tnumberb[:]
            ttnumberb.remove(c)
            for d in ttnumberb:
                tttnumberb = ttnumberb[:]
                tttnumberb.remove(d)
                for e in tttnumberb:
                    ttttnumberb = tttnumberb[:]
                    ttttnumberb.remove(e)
                    for ii in ttttnumberb:
                        numberi.append(ii)
                    for i in numberi:
                        tnumberi = numberi[:]
                        tnumberi.remove(i)
                        for j in tnumberi:
                            ttnumberi = tnumberi[:]
                            ttnumberi.remove(j)
                            for k in ttnumberi:
                                tttnumberi = ttnumberi[:]
                                tttnumberi.remove(k)
                                if a+i+j == b+j+k:
                                    for l in tttnumberi:
                                        ttttnumberi = tttnumberi[:]
                                        ttttnumberi.remove(l)
                                        m = ttttnumberi[0]
                                        if b+j+k == c+k+l == d+l+m == e+m+i:
                                            stopwatch = True
                                            res = int(str(a)+str(i)+str(j)+str(b)+str(j)+str(k)+str(c)+str(k)+str(l)+str(d)+str(l)+str(m)+str(e)+str(m)+str(i))
                                            print(res)
