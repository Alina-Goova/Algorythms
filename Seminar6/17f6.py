s=input().lower()
a=['']*(s.count(' ')+2)
alf='abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
n=0
for i in range(len(s)):
    if s[i] in alf:
        a[n]+=s[i]
    elif s[i]==' ' and a[n]!='':
        n+=1
a.remove('')
b=['']*len(a)
q=0
while q<len(b):
    k=0
    mini=100
    b[q]='я'*50
    for i in a:
        if i<b[q]:
            b[q]=i
    for j in range(len(a)):
        if a[j]==b[q]:
            a[j]='я'*51
    q+=1
for i in b:
    print(i, end=' ')
