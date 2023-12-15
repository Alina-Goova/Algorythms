def f2(s):
    for i in range(1, min(3, len(s))):
        s[0]*=s[i]
    return(s[0])

s=list(map(int, input().split()))
print(f2(s))
