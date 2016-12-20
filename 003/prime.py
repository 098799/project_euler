from sympy import primefactors

print(primefactors(600851475143)[-1])

# import math
# import time

# def checkprime(a):
#     for i in range(2,math.ceil(math.sqrt(a+0.001))):
#         if a%i == 0:
#             return False
#     return True

# def lprimfactor(a):
#     d = 2
#     lista = []
#     while a > 1:
#         if a%d == 0:
#             lista.append(d)
#             a //= d
#         else:
#             d+=1

#     return lista

#     # for i in range(2,math.ceil(a/2+0.1)):
#     #     if a%i == 0:
#     #        if checkprime(i):
#     #            print(i)
#     # return
        

# aa=time.process_time()
# j=600851475143
# #j=13195
# print(lprimfactor(j))
# bb=time.process_time()
# print(bb-aa)
