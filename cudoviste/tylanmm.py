R, C = map(int, input().split())
grid = [input() for _ in range(R)]
squash = [0]*5
for r in range(R-1):
    for c in range(C-1):
        if grid[r][c] == '#' or grid[r+1][c] == '#' or grid[r][c+1] == '#' or grid[r+1][c+1] == '#':
            continue
        squash[(grid[r][c] == 'X') + (grid[r+1][c] == 'X') + (grid[r][c+1] == 'X') + (grid[r+1][c+1] == 'X')] += 1
for s in squash:
    print(s)