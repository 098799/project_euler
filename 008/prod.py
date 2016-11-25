f=open('data','r')
full=''
for i in range(21):
    a=f.readline()
    full = full + a[:-1]

def adj(string,wheretostart,howmany):
    temp = 1
    for i in range(howmany):
        temp = temp * int(string[wheretostart+i])
    return temp

sohowmany=13

res=adj(full,0,sohowmany)
for i in range(1,len(full)-sohowmany+1):
    temp=adj(full,i,sohowmany)
    if temp>res:
        res=temp

print(res)
