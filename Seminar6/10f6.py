a=input().split()
n=int(input()) - 1
k=0
while k<len(a):
    k+=1
    n+=1
    if n==len(a):
        n=0
    print(a[n], end=' ')

#один два три четыре пять шесть семь
