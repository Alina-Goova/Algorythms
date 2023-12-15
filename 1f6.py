a1=[31, 24, 17]

b=[31, 24, 17]
a2=b

a3=[0]*3
n=0
for i in range(31, 16, -7):
    a3[n]=i
    n+=1

print(a1, a2, a3)

a4=[a1, a2, a3]
print(a4)
