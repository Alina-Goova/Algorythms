s='hh'

def pr(s):
    for i in s:
        k=0
        for j in s:
            if i==j:
                k+=1
                if k>1:
                    break
        if k>1:
            break
    if k>1:
        return False
    return True

while pr(s)==False:
    print('Ведите словарь:', end=' ')
    s=input()
    if pr(s)==False:
        print('Словарь введена неверно!')

a=['']*len(s)

for i in range(len(s)):
    a[i]=s[i]
print(a)
