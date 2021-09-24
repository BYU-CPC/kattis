for _ in range(int(input())):
    n, m = map(int, input().split())
    g = {i:[] for i in range(1, n+1)}
    for i in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    print(n-1)