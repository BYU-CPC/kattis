count = [0, 0]
for c in input():
    if c == 'W':
        count[0] += 1
    else:
        count[1] += 1
print(1 if count[0] == count[1] else 0)