from sys import stdin, stdout, setrecursionlimit
import heapq

setrecursionlimit(500000)

def _i():
    return stdin.readline()

def _p(x):
    stdout.write(str(x) + '\n')

x, y = map(int, _i().split())
q = []
grid = []
for i in range(y):
    grid.append(list(map(int, _i().split())))
    for j in range(x):
        heapq.heappush(q, (grid[i][j], i, j))

comps = [[-1]*x for _ in range(y)]
compHeights = []
comp_num = 0

def dfs(r, c, prev):
    if r < 0 or r >= y or c < 0 or c >= x:
        return
    
    if comps[r][c] != -1:
        compHeights[comp_num] = compHeights[comps[r][c]]
        return
    
    if grid[r][c] > prev:
        return
    
    comps[r][c] = comp_num
    dfs(r+1, c, grid[r][c])
    dfs(r-1, c, grid[r][c])
    dfs(r, c+1, grid[r][c])
    dfs(r, c-1, grid[r][c])

while q:
    h, r, c = heapq.heappop(q)
    if comps[r][c] == -1:
        compHeights.append(h)
        dfs(r, c, h)
        comp_num += 1

ans = 0
for i in range(y):
    for j in range(x):
        if compHeights[comps[i][j]] == grid[i][j]:
            ans += 1
_p(ans)

stdout.flush()