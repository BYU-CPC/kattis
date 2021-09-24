s = []
for c in input():
    if c == '<':
        s.pop()
    else:
        s.append(c)
print(''.join(s))