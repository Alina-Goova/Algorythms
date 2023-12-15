s1=input()
s2=input()
a=[s1, s2, len(s1), len(s2), '']
if s1>s2:
    a[4]='ПОСЛЕ'
else:
    a[4]='ДО'

print('output=', end='')
s=input()
if s=='lengths':
    print('Длины строк:', a[2], 'и', a[3])
elif s=='order':
    print('Строка "первая" идет', a[4], 'строки "вторая"')
