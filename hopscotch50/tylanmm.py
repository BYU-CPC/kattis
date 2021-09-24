n, k = map(int, input().split())
g = [[] for _ in range(k)]
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))
    for j in range(n):
        grid[i][j] -= 1
        g[grid[i][j]].append((i, j))

paths = [g[0][i] + (0,) for i in range(len(g[0]))]
for i in range(1, k):
    nextPaths = []
    if len(g[i]) == 0:
        paths = []
        break
    for r1, c1 in g[i]:
        loD = float('inf')
        for r2, c2, d in paths:
            loD = min(loD, d + abs(r1-r2) + abs(c1-c2))
        nextPaths.append((r1, c1, loD))
    paths = nextPaths

print(min(paths, key=lambda x: x[2])[2] if paths else -1)