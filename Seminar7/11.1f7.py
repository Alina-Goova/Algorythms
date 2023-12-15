r=input()
a=['']*len(r)
k=0

while r!='':
    mini=r[0]
    for i in r:
        if i<mini:
            mini=i
    for i in r:
        if i==mini:
            r=r.replace(mini, '')
    a[k]=mini
    k+=1
    if k==len(a):
        break

for i in a:
    if i!='':
        print(i, end=' ')
