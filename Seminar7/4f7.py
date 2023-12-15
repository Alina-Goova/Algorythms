print('Ведите строку:', end=' ')
s=input()

a=['']*(len(s)+1)

k1=0
for i in range(len(s)):
    k=0
    mini=s[0]
    for j in a:
        if j==s[i]:
            k=1
            break
    if k==1:
        continue
    else:
        a[k1]=s[i]
        k1+=1
b=[]
for i in a:
    if i!='':
        b.append(i)

b1=[0]*len(b)
for i in range(len(b)):
    for j in s:
        if b[i]==j:
            b1[i]+=1

alf='abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
k=0
for i in range(len(b)):
    if b[i] in alf:
        k+=b1[i]
print(k)
