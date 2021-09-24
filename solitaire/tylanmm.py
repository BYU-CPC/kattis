from copy import deepcopy
from collections import deque

def bfs(grid):
    seen = set()
    q = deque()
    q.append((grid, 0))
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    best = 0
    while q:
        curr, moves = q.popleft()
        rep = '\n'.join([''.join(line) for line in curr])
        if rep in seen:
            continue
        best = max(best, moves)
        #print(rep)
        seen.add(rep)


        for i in range(len(curr)):
            for j in range(len(curr[0])):
                # if we're not on a peg, just skip
                if curr[i][j] != 'o':
                    continue

                for di, dj in dirs:
                    # if the landing spot is in bounds, and the jumped spot has a peg, and the landing spot is empty
                    if (0 <= i+di*2 < len(curr)) and (0 <= j+dj*2 < len(curr[0])) and curr[i+di][j+dj] == 'o' and curr[i+di*2][j+dj*2] == '.':
                        new = deepcopy(curr)
                        new[i][j] = '.'
                        new[i+di][j+dj] = '.'
                        new[i+di*2][j+dj*2] = 'o'
                        q.append((new, moves+1))
    
    return best

n = int(input())
for _ in range(n):
    grid = []
    line = input()
    while line:
        grid.append(list(line))
        try:
            line = input()
        except EOFError:
            line = ''
    start = ''.join([''.join(line) for line in grid]).count('o')
    moves = bfs(grid)
    print(start - moves, moves)
    