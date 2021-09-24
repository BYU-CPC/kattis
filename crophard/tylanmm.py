def choose(n, k):
    num = 1
    den = 1
    for i in range(1, min(k, n-k) + 1):
        num *= n
        den *= i
        n -= 1
    return num // den

for t in range(int(input())):
    n, A, B, C, D, x, y, M = map(int, input().split())
    rem = [[0]*3 for _ in range(3)]
    rem[x%3][y%3] += 1
    for i in range(n-1):
        x = (A*x + B) % M
        y = (C*y + D) % M
        rem[x%3][y%3] += 1
    
    count = 0
    pos = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
    for i in range(0, 9):
        for j in range(i, 9):
            for k in range(j, 9):
                if ((pos[i][0] + pos[j][0] + pos[k][0]) % 3 == 0) and ((pos[i][1] + pos[j][1] + pos[k][1]) % 3 == 0):
                    if len({i, j, k}) > 1:
                        count += rem[pos[i][0]][pos[i][1]] * rem[pos[j][0]][pos[j][1]] * rem[pos[k][0]][pos[k][1]]
                    elif rem[pos[i][0]][pos[i][1]] > 2:
                        n = rem[pos[i][0]][pos[i][1]]
                        count += choose(n, 3)

    print(f'Case #{t+1}: {count}')