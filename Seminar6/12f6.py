s=input()
cf='0123456789'

a=['']*len(s)
n=0
for i in s:
    if i in cf:
        a[n]+=i
    elif a[n]!='':
        n+=1
k=0
for i in a:
    if i!='':
        k+=1
b=[0]*k
for j in range(len(b)):
    b[j]=int(a[j])
mr=0
for j in b:
    k=0
    for j1 in b:
        if j>=j1:
            k+=1
    if k==2:
        print(j)
        for q in range(len(b)):
            if j==b[q]:
                print(q)
                break
        mr=1
if mr==0:
    print('Такого числа нет.')
