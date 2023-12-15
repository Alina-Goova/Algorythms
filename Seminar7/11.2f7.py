b=[]
for i in range(50):
    s=input()
    if s=='':
        break
    a=s.split()
    b.append(a[0])
    b.append(a[-1])    
for i in b:
    print(i, end=' ')
