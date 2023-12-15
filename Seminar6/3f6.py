a=input().split()
mr=0
for i in a:
    if i=='repeat':
        mr=1
        break
q=a[len(a)-1]
for i in q:
    if not(i in '01256789'):
        mr=0
        break

if mr==0:
    print('Список не подвергается изменениям')
else:
    q1=int(q)
    b=['']*((len(a)-2)*q1 + 2)
    k=len(a)-2
    k1=0
    for j in range(q1):
        for j1 in range(k):
            b[j1+k1]=a[j1]
        k1+=k
    b[len(b)-2]=a[len(a)-2]
    b[len(b)-1]=a[len(a)-1]

print(a)
print(b)
