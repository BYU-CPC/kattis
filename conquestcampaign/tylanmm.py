from collections import deque

r, c, n = map(int, input().split())
occ = [[False]*(c+1) for _ in range(r+1)]
q = deque()
for _ in range(n):
    R, C = map(int, input().split())
    q.append((R, C, 1))

numDays = 0
while q:
    R, C, d = q.popleft()
    if occ[R][C]: continue
    occ[R][C] = True
    numDays = max(numDays, d)

    if R + 1 <= r:
        q.append((R+1, C, d+1))
    if R - 1 > 0:
        q.append((R-1, C, d+1))
    if C + 1 <= c:
        q.append((R, C+1, d+1))
    if C - 1 > 0:
        q.append((R, C-1, d+1))
print(numDays)