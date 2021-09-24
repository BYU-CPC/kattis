def solve():
    res = [['N']*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if grid[i][j]:
                if rowSum[i] > 1 and colSum[j] > 1:
                    res[i][j] = 'I'
                else:
                    res[i][j] = 'P'
            else:
                if rowSum[i] and colSum[j]:
                    print('impossible')
                    return
    
    for row in res:
            print(''.join(row))

for _ in range(int(input())):
    r, c = map(int, input().split())
    grid = [list(map(int, input())) for _ in range(r)]
    rowSum = [sum(grid[i]) for i in range(r)]
    colSum = [sum([grid[i][j] for i in range(r)]) for j in range(c)]
    solve()
    print('-'*10)