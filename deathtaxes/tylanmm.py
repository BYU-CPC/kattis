s, c = 0, 0
line = input().split()
while line[0] != 'die':
    if line[0] == 'buy':
        x, y = map(int, line[1:])
        s, c = s+x, (x*y + s*c)/(x+s)
    elif line[0] == 'sell':
        x, y = map(int, line[1:])
        s -= x
    elif line[0] == 'split':
        x = int(line[1])
        s *= x
        c /= x
    elif line[0] == 'merge':
        x = int(line[1])
        s //= x
        c *= x
    line = input().split()

y = int(line[1])
print(s*(y - (0 if y < c else y - c)*0.3))