from heapq import heappop, heappush

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
seen = [[False]*n for _ in range(n)]

q = [(0, 0, 0)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while q:
    d, r, c = heappop(q)
    if seen[r][c]: continue
    seen[r][c] = True
    if r == n-1 and c == n-1:
        print(d)
        break

    for dr, dc in dirs:
        ri, ci = r+dr, c+dc
        if 0 <= ri < n and 0 <= ci < n:
            heappush(q, (max(d, grid[ri][ci]), ri, ci))