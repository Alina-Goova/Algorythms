def calc(s):
    s = s.replace('^', '**', 1)
    s = s.replace('/', '//', 1)
    return eval(s)

print(calc(input()))
