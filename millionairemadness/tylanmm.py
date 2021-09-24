import heapq

m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
pq = [(0, 0, 0)]
hi = 0

while pq:
    d, i, j = heapq.heappop(pq)
    if grid[i][j] == -1: continue
    hi = max(hi, d)
    if i == m-1 and j == n-1:
        break

    if i:
        heapq.heappush(pq, (grid[i-1][j] - grid[i][j], i-1, j))
    if j:
        heapq.heappush(pq, (grid[i][j-1] - grid[i][j], i, j-1))
    if i + 1 < m:
        heapq.heappush(pq, (grid[i+1][j] - grid[i][j], i+1, j))
    if j + 1 < n:
        heapq.heappush(pq, (grid[i][j+1] - grid[i][j], i, j+1))

    grid[i][j] = -1

print(hi)