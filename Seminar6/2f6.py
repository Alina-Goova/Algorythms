s=input().lower()

alf='abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
cf='0123456789'

k=0
for j in s:
    if j in cf:
        k+=1

a1=['']*len(s)
a2=['']*(s.count(' ')+1)
a3=['']*k

n=0
k=0
for i in range(len(s)):
    a1[i]=s[i]
    if s[i] in alf:
        a2[n]+=s[i]
    elif s[i]==' ' and a2[n]!='':
        n+=1
    if s[i] in cf:
        a3[k]=s[i]
        k+=1

print(a1, a2, a3)
