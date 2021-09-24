m, n = map(int, input().split())
grid = [list(input()) for _ in range(m)]

def flood(r, c):
    if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '#':
        return
    
    grid[r][c] = '.'
    flood(r+1, c)
    flood(r-1, c)
    flood(r, c+1)
    flood(r, c-1)
    flood(r+1, c+1)
    flood(r+1, c-1)
    flood(r-1, c+1)
    flood(r-1, c-1)

count = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == '#':
            flood(i, j)
            count += 1
print(count)