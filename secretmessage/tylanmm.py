from math import ceil
for _ in range(int(input())):
    s = input()
    l = len(s)
    m = ceil(l**0.5)
    grid = [['*']*m for _ in range(m)]
    
    i = 0
    for c in range(m-1, -1, -1):
        for r in range(m):
            grid[r][c] = s[i]
            i += 1
            if i == l:
                break
        else:
            continue
        break
    
    res = []
    for i in range(m):
        for j in range(m):
            if grid[i][j] != '*':
                res.append(grid[i][j])
    
    print(''.join(res))