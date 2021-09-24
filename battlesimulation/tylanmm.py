moves = input()
n = len(moves)
i = 0
combo = {'R', 'B', 'L'}
res = []
while i < n:
    if i <= n-3 and set(moves[i:i+3]) == combo:
        res.append('C')
        i += 3
    else:
        if moves[i] == 'R':
            res.append('S')
        elif moves[i] == 'B':
            res.append('K')
        else:
            res.append('H')
        i += 1
print(''.join(res))