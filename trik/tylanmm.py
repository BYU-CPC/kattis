moves, pos = input(), [1, 0, 0]
for m in moves:
    if m == 'A':
        pos[0], pos[1] = pos[1], pos[0]
    elif m == 'B':
        pos[1], pos[2] = pos[2], pos[1]
    else:
        pos[0], pos[2] = pos[2], pos[0]
print(pos.index(1) + 1)