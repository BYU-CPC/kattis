from collections import deque
from sys import stdin

dirs = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

for line in stdin:
    r, c, gr, gc, lr, lc, = map(int, line.split())
    visited = [[False]*c for _ in range(r)]
    q = deque([(gr-1, gc-1, 0)])

    while q:
        i, j, d = q.popleft()
        if i < 0 or i >= r or j < 0 or j >= c or visited[i][j]:
            continue
        visited[i][j] = True

        if i+1 == lr and j+1 == lc:
            print(d)
            break

        for x, y in dirs:
            q.append((i+x, j+y, d+1))
    else:
        print('impossible')