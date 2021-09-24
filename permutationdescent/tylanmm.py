for _ in range(int(input())):
    k, n, v = map(int, input().split())
    ways = [[0]*n for _ in range(n+1)]
    ways[0][0] = 1
    for i in range(1, n+1):
        for j in range(i):
            ways[i][j] = ways[i-1][j] * (j+1)
            if j: ways[i][j] += ways[i-1][j-1] * (i - j)
    print(k, ways[n][v] % 1001113)