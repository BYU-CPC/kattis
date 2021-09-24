import heapq

n, m = map(lambda x: int(x)+2, input().split())
tree = ['.'*(m+2)] + ['.'+input()+'.' for _ in range(n-2)] + ['.'*(m+2)]

hi = 0
ans = [[0]*m for i in range(n)]
seen = [[False]*m for i in range(n)]
q = [(0, i, j) for j in range(m) for i in range(n) if tree[i][j] == '.']
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    ring, r, c = heapq.heappop(q)
    if r < 0 or r == n or c < 0 or c == m or seen[r][c]:
        continue
    seen[r][c] = True
    ans[r][c] = ring if tree[r][c] == 'T' else 0
    hi = max(hi, ring)
    for dr, dc in dirs:
        heapq.heappush(q, (ring+1, r+dr, c+dc))

size = 2 if hi < 10 else 3
for i in range(1, n-1):
    for j in range(1, m-1):
        if hi < 10:
            print('{:.>2s}'.format(str(ans[i][j]) if ans[i][j] else '.'), end='')
        else:
            print('{:.>3s}'.format(str(ans[i][j]) if ans[i][j] else '.'), end='')
    print()