from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input())) for _ in range(n)]
seen = [[False]*m for _ in range(n)]
q = deque()
q.append((0, 0, 0))

ans = -1
while q:
    r, c, d = q.popleft()
    if seen[r][c]: continue
    seen[r][c] = True
    if r + 1 == n and c + 1 == m:
        ans = d
        break
    step = grid[r][c]
    if c + step < m:
        q.append((r, c+step, d+1))
    if c - step >= 0:
        q.append((r, c-step, d+1))
    if r + step < n:
        q.append((r+step, c, d+1))
    if r - step >= 0:
        q.append((r-step, c, d+1))
print(ans)