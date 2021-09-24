from collections import deque

n = int(input())
grid = []
for i in range(n):
    line = input()
    if 'K' in line:
        R, C = i, line.index('K')
    grid.append(list(line))
q = deque()
q.append((C, R, 0))
grid[R][C] = '.'

while q:
    C, R, j = q.popleft()
    if grid[R][C] != '.':
        continue
    
    if R == 0 and C == 0:
        print(j)
        break
    
    grid[R][C] = '#'
    
    if C - 2 >= 0:
        if R - 1 >= 0:
            q.append((C-2, R-1, j+1))
        if R + 1 < n:
            q.append((C-2, R+1, j+1))
    
    if C + 2 < n:
        if R - 1 >= 0:
            q.append((C+2, R-1, j+1))
        if R + 1 < n:
            q.append((C+2, R+1, j+1))
    
    if R - 2 >= 0:
        if C - 1 >= 0:
            q.append((C-1, R-2, j+1))
        if C + 1 < n:
            q.append((C+1, R-2, j+1))
    
    if R + 2 < n:
        if C - 1 >= 0:
            q.append((C-1, R+2, j+1))
        if C + 1 < n:
            q.append((C+1, R+2, j+1))
else:
    print(-1)