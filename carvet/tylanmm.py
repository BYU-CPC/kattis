from collections import deque

m, n = map(int, input().split())
sr, sc = 0, 0
grid = []
for i in range(m):
    row = list(map(int, input().split()))
    if -1 in row:
        sr, sc = i, row.index(-1)
    grid.append(row)
r, c = map(int, input().split())

visited = [[False]*n for _ in range(m)]
q = deque([(sr, sc, [])])
p = []
while q:
    i, j, path = q.popleft()
    if visited[i][j]:                                   # been here already
        continue
    if i == r-1 and j == c-1:                           # found target
        if p:
            if len(path) > len(p):
                break
            p = min(p, path)
        else:
            p = path
        continue    
    
    visited[i][j] = True
    if i > 1 and grid[i-1][j] == grid[i-2][j]:          # can move above car down
        q.append((i-2, j, path+[grid[i-2][j]]))
    if i + 2 < m and grid[i+1][j] == grid[i+2][j]:      # can move below car up
        q.append((i+2, j, path+[grid[i+2][j]]))
    if j > 1 and grid[i][j-1] == grid[i][j-2]:          # can move left car right
        q.append((i, j-2, path+[grid[i][j-2]]))
    if j + 2 < n and grid[i][j+1] == grid[i][j+2]:      # can move right car left
        q.append((i, j+2, path+[grid[i][j+2]]))

if p:
    print(*p)
else:
    print('impossible')